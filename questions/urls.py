from rest_framework import routers
from django.urls import path
from .views import QuestionCreate, QuestionDetailView, QuestionListView

app_name='questions'



urlpatterns = [
	path('create/', QuestionCreate.as_view(), name='ask-question'),
	path('list/', QuestionListView.as_view(), name='question-list'),
	path('<pk>/', QuestionDetailView.as_view(), name='question-detail')
]



