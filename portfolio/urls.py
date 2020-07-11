from django.urls import path, include

from . import views

app_name = 'portfoilo'

urlpatterns = [
    path('profile/', views.HomeView, name='home-page'),
]
