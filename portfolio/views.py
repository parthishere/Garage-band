from django.shortcuts import (
    render,
    reverse,
    redirect,
    HttpResponse,
    Http404,
    get_object_or_404,
    get_list_or_404
)
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin


from django.db.models import Q


from friendship.models import Friend, Follow, Block
from .models import UserProfileModel, User
from questions.models import Questions
from answers.models import Answers



@login_required
def HomeView(request):
    """ HOME VIEW FOR PORTFOIO PAGE """
    if request.user.is_authenticated:
        qs = Questions.objects.filter(user=request.user)
        answer_qs = Answers.objects.filter(user=request.user)
        followers = Follow.objects.followers(request.user)
        following = Follow.objects.following(request.user)
        context = {
            'qs': qs,
            'followers': followers,
            'following': following,
            'answer_qs': answer_qs,
        }
        return render(request, 'portfolio/portfolio.html', context)
    else:
        context = {

        }
        return render(request, 'portfolio/404.html', context)



# class SearchProfileView(ListView):
#     """ Search Profile view """
#     template_name = 'portfolio/search-list.html'
#     model=UserProfileModel
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         request = self.request
#         try:
#             query = request.GET.get('q')
#             search_name = request.GET.get('search')
#         except:
#             raise Http404('q not found in Url')
#         if search_name is not None:
#             if search_name == 'question':
#                 if query is not None:
#                     obj_list = (
#                         Q(title__icontains=query) | Q(tags__tag_name__icontains=query)
#                     )
#                     context['object_list'] = Questions.objects.filter(obj_list).distinct()
#                     context['query'] = query
#                     return context
#             elif search_name=='profile':
#                 blocked_user_list = Block.objects.blocked(request.user)
#                 if query is not None:
#                     obj_list = (
#                         Q(user__username__icontains=query) | Q(about__icontains=query) | Q(profession__icontains=query) | Q(softwear__icontains=query) | Q(awards__icontains=query)
#                         # & ~Q(user=[u for u in blocked_user_list])
#                     )
#                     context['object_list'] = UserProfileModel.objects.filter(obj_list).distinct()
#                     context['query'] = query
#                     return context
#         else:
#             context['objects_list'] = None
#             context['massage'] = "Please selact what you want to search!"
#             return context



class ProfileDetailView(DetailView, LoginRequiredMixin):
    """ Profile Detail View """
    model=UserProfileModel
    template_name= 'portfolio/profile-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        request = self.request
        blocked_user_list = Block.objects.blocked(self.object.user)
        context['qs'] = Questions.objects.filter(user=self.object.user)
        context['followers'] = Follow.objects.followers(self.object.user)
        context['following'] = Follow.objects.following(self.object.user)
        context['blocked'] = Block.objects.blocked(request.user)
        return context



class UpdateProfileView(UpdateView, LoginRequiredMixin):
    """ Edit Profile View """
    model = UserProfileModel
    fields = '__all__'
    template_name = 'portfolio/edit-profile.html'



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
    """ Make request.user a follower of other_user:"""
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if request.user == other_user or Follow.objects.follows(request.user, other_user.user):
        return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))
    else:
        try:
            Follow.objects.add_follower(request.user, other_user.user)
        except:
            return Http404('User already Follows Other User')
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))



@login_required
def remove_follower_user(request, other_user_pk):
    """ Make request.user unfollowes of other_user: """
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if Follow.objects.follows(request.user, other_user.user):
        try:
            Follow.objects.remove_follower(request.user, other_user.user)
        except:
            return Http404("User already removed")
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))



@login_required
def block_user(request, other_user_pk):
    """ Make request.user block other_user: """
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if request.user != other_user or other_user.user in Block.objects.blocked(request.user):
        if Follow.objects.follows(request.user, other_user.user):
            try:
                Follow.objects.remove_follower(request.user, other_user.user)
            except:
                return Http404("already removed")
        return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))
    else:
        Block.objects.add_block(request.user, other_user.user)
        if Follow.objects.follows(request.user, other_user.user):
            try:
                Follow.objects.remove_follower(request.user, other_user.user)
            except:
                return Http404("already removed")
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))



@login_required
def unblock_user(request, other_user_pk):
    """ Make request.user unblock other_user: """
    other_user = get_object_or_404(UserProfileModel, pk=other_user_pk)
    if other_user.user in Block.objects.blocked(request.user):
        try:
            Block.objects.remove_block(request.user, other_user.user)
        except:
            return Http404("alreay unblocked")
    return redirect(reverse('portfolio:detail', kwargs={'slug':other_user.slug}))

@login_required
def follower_list(request, pk):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=pk)
        if request.user in Follow.objects.followers(user):
            list_follower = Follow.objects.followers(user)
        else:
            pass
