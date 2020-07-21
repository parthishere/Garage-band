from rest_framework import routers
from django.urls import path
from .views import ( 
	AnswerDetailView, 
	AnswerDeleteView,
	AnswerUpdateView,
)

app_name='answers'



urlpatterns = [
	path('delete/<pk>', AnswerDeleteView.as_view(), name='delete'),
	path('update/<pk>', AnswerUpdateView.as_view(), name='update'),
	path('<pk>/', AnswerDetailView.as_view(), name='detail'),
]



