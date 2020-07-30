from django.urls import path, include

from .views import (
    HomeView,
    UpdateProfileView,
    SearchProfileView,
    ProfileDetailView,
    add_follower_user,
    remove_follower_user,
    block_user,
    unblock_user,
)

app_name = 'portfoilo'

urlpatterns = [
    path('profile/', HomeView, name='home'),
    path('profile/edit/<pk>', UpdateProfileView.as_view() , name='edit'),
    path('profile/search', SearchProfileView.as_view(), name='search-cbv'),
    path('profile/<slug>', ProfileDetailView.as_view(), name='detail'),
    path('profile/follow/<int:other_user_pk>', add_follower_user, name='follow'),
    path('profile/unfollow/<int:other_user_pk>', remove_follower_user, name='remove-follow'),
    path('profile/block/<int:other_user_pk>', block_user, name='block'),
    path('profile/unblock/<int:other_user_pk>', unblock_user, name='unblock'),
    # path('profile/follow/<int:pk>', views.add_followers_view, name='add_follower')
]
