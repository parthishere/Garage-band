from django.urls import path, include

from . import views

app_name = 'portfoilo'

urlpatterns = [
    path('', views.HomeView, name='home-page'),
]
