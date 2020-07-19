from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.db.models import Q
# from actstream.actions import follow, unfollow


from .models import UserProfileModel
from questions.models import Questions


# Create your views here.
def HomeView(request):
    """ HOME VIEW FOR PORTFOIO PAGE """
    qs = Questions.objects.filter(user=request.user)
    context = {
        'qs': qs,
    }
    # if request.user.is_authenticated:
    #     user_instance = UserProfileModel.objects.filter(user=request.user)
    #     # session_id = request.session.get('user_id'==request.user.id)
    #     if user_instance.exists():
    #         context = {
    #             'user': user_instance,
    #         }
    #         return render(request, 'portfolio/portfolio.html', context=context)
    #     else:
    #         user_instance = UserProfileModel.objects.create(user=request.user)
    #         request.session['user_id'] = request.user.id
    #         context = {
    #             'user': user_instance,
    #         }
    #         return render(request, '/portfolio/portfolio.html', context=context)
    # else:
    #     return redirect('account_login')
    return render(request, 'portfoilo/portfoilo.html', context)



@login_required        
def add_followers_view(request, pk):
    """ Pk is requested following user's primary key and instance is you as a user(who sent follow request) instance, So don't get confused """
    requested_user = UserProfileModel.objects.get(pk=pk)
    user = UserProfileModel.objects.get(user=request.user)
    requested_user.following.add(user)
    requested_user.save()
    return reverse('portfolio:profile-detail', kwargs={'pk': pk})
    


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
        
        
