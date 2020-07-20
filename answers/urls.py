from rest_framework import routers
from django.urls import path
from .views import ( 
	AnswerDetailView, 
	AnswerDeleteView,
	AnswerUpdateView,
)

app_name='answers'



urlpatterns = [
	path('delete/<pk>', QuestionDeleteView.as_view(), name='delete'),
	path('update/<pk>', QuestionUpdateView.as_view(), name='update'),
	path('<pk>/', QuestionDetailView.as_view(), name='detail'),
]



