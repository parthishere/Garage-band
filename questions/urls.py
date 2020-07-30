from rest_framework import routers
from django.urls import path
from .views import (
	QuestionCreate,
	QuestionDetailView,
	QuestionListView,
	upvote_create,
	downvote_create,
	QuestionDeleteView,
	QuestionUpdateView,
	SearchQuestionView,
	question_downvote_create,
	question_upvote_create
)

app_name='questions'



urlpatterns = [
	path('create/', QuestionCreate.as_view(), name='ask-question'),
	path('delete/<pk>', QuestionDeleteView.as_view(), name='delete'),
	path('update/<pk>', QuestionUpdateView.as_view(), name='update'),
	path('list/', QuestionListView.as_view(), name='list'),
	path('<pk>/', QuestionDetailView.as_view(), name='detail'),
	path('like/<pk>/<q_pk>', upvote_create, name='like'),
	path('dislike/<pk>/<q_pk>', downvote_create, name='dislike'),
	path('like/<pk>', question_upvote_create, name='question-like'),
	path('dislike/<pk>', question_downvote_create, name='question-dislike'),
	path('search', SearchQuestionView.as_view(), name='search'),
]
