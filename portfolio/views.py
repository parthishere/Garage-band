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
        
        
