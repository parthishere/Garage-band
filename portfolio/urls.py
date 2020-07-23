from django.urls import path, include

from . import views

app_name = 'portfoilo'

urlpatterns = [
    path('profile/', views.HomeView, name='home'),
    path('profile/search', views.SearchProfileView.as_view(), name='search-cbv'),
    path('profile/<slug>', views.ProfileDetailView.as_view(), name='detail'),
    path('profile/follow/<int:other_user_pk>', views.add_follower_user, name='follow'),
    path('profile/unfollow/<int:other_user_pk>', views.remove_follower_user, name='remove-follow'),
    path('profile/block/<int:other_user_pk>', views.block_user, name='block'),
    path('profile/unblock/<int:other_user_pk>', views.unblock_user, name='unblock'),
    # path('profile/follow/<int:pk>', views.add_followers_view, name='add_follower')
]
