from django.shortcuts import render, reverse, redirect, HttpResponse

from .models import UserProfileModel

# Create your views here.
def HomeView(request):
    if request.user.is_authenticated:
        user_instance = UserProfileModel.objects.filter(user=request.user)
        # session_id = request.session.get('user_id'==request.user.id)
        if user_instance.exists():
            context = {
                'user': user_instance,
            }
        else:
            user_instance = UserProfileModel.objects.create(user=request.user)
            request.session['user_id'] = request.user.id
            context = {
                'user': user_instance,
            }
            return render(request, 'portfoilo/portfolio.html', context=context)
    else:
        return HttpResponse("Chall hutt bkl")
            
             
        
        


