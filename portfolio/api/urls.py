from django.urls import path, include

from .views import (
    ProfileCreateAPIView,
    ProfileListAPIView,
    ProfileRUDView,
    follow_create_api
)

app_name = 'portfolio-api'

urlpatterns = [
    path('create/', ProfileCreateAPIView.as_view(), name='create-api'),
    path('list/', ProfileListAPIView.as_view(), name='list-api'),
    path('<pk>/', ProfileRUDView.as_view(), name='rud-api'),
    path('<pk>/follow', follow_create_api, name='follow-api'),
    path('<pk>/unfollow', ProfileRUDView.as_view(), name='rud-api'),
]

