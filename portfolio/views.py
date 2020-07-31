from django.shortcuts import render, reverse, redirect, HttpResponse, Http404, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.db.models import Q


from friendship.models import Friend, Follow, Block
from .models import UserProfileModel, User
from questions.models import Questions
from answers.models import Answers


# Create your views here.
@login_required
def HomeView(request):
    """ HOME VIEW FOR PORTFOIO PAGE """
    if request.user.is_authenticated:
        qs = Questions.objects.filter(user=request.user)
        answer_qs = Answers.objects.filter(user=request.user)
        user = UserProfileModel.objects.get(user=request.user)
        followers = Follow.objects.followers(request.user)
        following = Follow.objects.following(request.user)
        context = {
            'qs': qs,
            'user': user,
            'followers': followers,
            'following': following,
            'answer_qs': answer_qs,
        }
        return render(request, 'portfolio/portfolio.html', context)
    else:
        context = {

        }
        return render(request, 'portfolio/404.html', context)

    


class SearchProfileView(ListView):
    template_name = 'portfolio/search-list.html'
    model=UserProfileModel
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        request = self.request
        try:
            query = request.GET.get('q')
            search_name = request.GET.get('search')
        except:
            raise Http404('q not found in Url')
        if search_name == 'question':
            if query is not None:
                obj_list = (
                    Q(question__icontains=query) | Q(tags__icontains=query) 
                )
                context['object_list'] = Questions.objects.filter(obj_list).distinct()
                context['query'] = query
                return context
        elif search_name=='profile':
            if query is not None:
                obj_list = (
                    Q(user__username__icontains=query) | Q(about__icontains=query) | Q(profession__icontains=query) | Q(softwear__icontains=query) | Q(awards__icontains=query)
                )
                context['object_list'] = UserProfileModel.objects.filter(obj_list).distinct()
                context['query'] = query
                return context
        else:
            return UserProfileModel.get_featured_profile()

 

class ProfileDetailView(DetailView, LoginRequiredMixin):
    model=UserProfileModel
    template_name= 'portfolio/profile-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs) 
        context['qs'] = get_list_or_404(Questions, user=self.object.user)
        context['followers'] = Follow.objects.followers(self.object.user)
        context['following'] = Follow.objects.following(self.object.user)
        context['blocked'] = Block.objects.blocked(self.object.user)
        return context
        
        
def list_of_friends(request, user):
    list_of_friends = Friend.objects.friends(user)
    list_of_followers = Follow.objects.followers(request.user)
    list_of_following = Follow.objects.following(request.user)
    context = {
        'list': list_of_friends, 
    }
    return reder(request, 'portfoilo/list-friend.html', context)

@login_required
def add_follower_user(request, other_user_pk):
    #### Make request.user a follower of other_user:
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if Follow.objects.follows(request.user, other_user.user):
        return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))
    else:
        Follow.objects.add_follower(request.user, other_user.user)      
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))

@login_required
def remove_follower_user(request, other_user_pk):
    #### Make request.user unfollowes of other_user:
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if Follow.objects.follows(request.user, other_user.user):
        Follow.objects.remove_follower(request.user, other_user.user)
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))

@login_required
def block_user(request, other_user_pk):
    #### Make request.user block other_user:
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if other_user.user in Block.objects.blocked(request.user):
        return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))
    else:    
        Block.objects.add_block(request.user, other_user.user)
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))

@login_required
def unblock_user(request, other_user_pk):
    #### Make request.user unblock other_user:
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if other_user.user in Block.objects.blocked(request.user):
        Block.objects.remove_block(request.user, other_user.user)
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))

class UpdateProfileView(UpdateView, LoginRequiredMixin):
    model = UserProfileModel
    fields = '__all__'
    template_name = 'portfolio/edit-profile.html'