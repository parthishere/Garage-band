from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView


from django.db.models import Q


from friendship.models import Friend, Follow, Block
from .models import UserProfileModel
from questions.models import Questions
from answers.models import Answers


# Create your views here.
@login_required
def HomeView(request):
    """ HOME VIEW FOR PORTFOIO PAGE """
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

    


class SearchProfileView(ListView):
    template_name = 'portfolio/search-list.html'
    model=UserProfileModel
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        request = self.request
        query = request.GET.get('q')
        
        if query is not None:
            obj_list = (
                Q(user__username__icontains=query) | Q(about__icontains=query) | Q(profession__icontains=query) | Q(softwear__icontains=query) | Q(awards__icontains=query)
            )
            context['object_list'] = UserProfileModel.objects.filter(obj_list).distinct()
            context['query'] = query
            return context
        else:
            return UserProfileModel.get_featured_profile()

 

class ProfileDetailView(DetailView):
    model=UserProfileModel
    template_name= 'portfolio/profile-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['qs'] = Questions.objects.filter(user=self.object.user)
        context['followers'] = Follow.objects.followers(self.object.user)
        context['following'] = Follow.objects.following(self.object.user)
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
    other_user = UserProfileModel.objects.get(pk=other_user_pk)
    Follow.objects.add_follower(request.user, other_user.user)      
    
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))

@login_required
def remove_follower_user(request, other_user_pk):
    other_user = UserProfileModel.objects.get(pk=other_user_pk)
    Follow.objects.remove_follower(request.user, other_user.user)
    
    return redirect(reverse('portfolio:detail', kwargs={'pk':other_user_pk}))

@login_required
def block_user(request, other_user_pk):
    #### Make request.user block other_user:
    other_user = UserProfileModel.objects.get(pk=other_user_pk)
    Block.objects.add_block(request.user, other_user.user)
    # context = {
    #     'list': list_of_friends, 
    # }
    return redirect(reverse('portfolio:detail', kwargs={'pk':other_user_pk}))

@login_required
def unblock_user(request, other_user_pk):
    #### Make request.user unblock other_user:
    other_user = UserProfileModel.objects.get(pk=other_user_pk)
    Block.objects.remove_block(request.user, other_user.user)
    # context = {
    #     'list': list_of_friends, 
    # }
    return redirect(reverse('portfolio:detail', kwargs={'pk':other_user_pk}))

class UpdateProfileView(UpdateView):
    model = UserProfileModel
    fields = '__all__'
    template_name = 'portfolio/edit-profile.html'