from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import UserProfileModel

# Create your views here.
def HomeView(request):
    """ HOME VIEW FOR PORTFOIO PAGE """
    if request.user.is_authenticated:
        user_instance = UserProfileModel.objects.filter(user=request.user)
        # session_id = request.session.get('user_id'==request.user.id)
        if user_instance.exists():
            context = {
                'user': user_instance,
            }
            return render(request, 'portfolio/portfolio.html', context=context)
        else:
            user_instance = UserProfileModel.objects.create(user=request.user)
            request.session['user_id'] = request.user.id
            context = {
                'user': user_instance,
            }
            return render(request, '/portfolio/portfolio.html', context=context)
    else:
        return redirect('account_login')

@login_required        
def add_followers_view(request):
    pass

        
        
