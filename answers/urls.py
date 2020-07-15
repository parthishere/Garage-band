from django.urls import path

from . import views

app_name = 'answer'


urlpatterns = [
    path('', views.AnswerListView.as_view(), name='answers'),
    path('question/<slug>/answer/', views.AnswerCreate.as_view(), name='answer-add'),
    path('answer/<slug>/comment/', views.CommentCreate.as_view(), name='comment-add'),
    path('answer/upvote/<slug>', views.UpvoteCreate.as_view(), name='answer-upvote'),
    path('answer/downvote/<slug>', views.DownvoteCreate.as_view(), name='answer-downvote'),

]
