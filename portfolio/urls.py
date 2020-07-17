from django.urls import path, include

from . import views

app_name = 'portfoilo'

urlpatterns = [
    path('profile/', views.HomeView, name='home-page'),
    path('profile/search', views.SearchProfileView.as_view(), name='search-cbv'),
    path('profile/<slug>', views.ProfileDetailView.as_view(), name='profile-detail-cbv'),
    # path('profile/follow/<int:pk>', views.add_followers_view, name='add_follower')
]
