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
	# search_question,
	question_downvote_create,
	question_upvote_create,
	QuestionDraftListView,
	save_question,
	SavedQuestionListView
)

app_name='questions'



urlpatterns = [
	path('create/', QuestionCreate.as_view(), name='ask-question'),
	path('draft/', QuestionDraftListView.as_view(), name='draft'),
	path('saved-questions/', SavedQuestionListView.as_view(), name='save'),
	path('save/<pk>', save_question, name='save'),
	path('delete/<pk>', QuestionDeleteView.as_view(), name='delete'),
	path('update/<pk>', QuestionUpdateView.as_view(), name='update'),
	path('list/', QuestionListView.as_view(), name='list'),
	path('<pk>/', QuestionDetailView.as_view(), name='detail'),
	path('like/<pk>/<q_pk>', upvote_create, name='like'),
	path('dislike/<pk>/<q_pk>', downvote_create, name='dislike'),
	path('like/<pk>', question_upvote_create, name='question-like'),
	path('dislike/<pk>', question_downvote_create, name='question-dislike'),
	# path('search', search_question, name='search'),
]
