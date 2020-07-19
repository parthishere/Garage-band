from django.urls import path,re_path

from . import views

app_name = 'answer'


urlpatterns = [
    path('', views.AnswerListView.as_view(), name='answers'),
    re_path('question/(?P<slug>[\w-]+)/answer/', views.AnswerCreate.as_view(), name='answer-add'),
    re_path('answer/(?P<slug>[\w-]+)/comment/', views.CommentCreate.as_view(), name='comment-add'),
    re_path('answer/upvote/(?P<slug>[\w-]+)', views.UpvoteCreate.as_view(), name='answer-upvote'),
    re_path('answer/downvote/(?P<slug>[\w-]+)', views.DownvoteCreate.as_view(), name='answer-downvote'),
    re_path('(?P<slug>[\w-]+)/delete',views.AnswerDelete.as_view(),name='delete'),
    re_path('/(?P<slug>[\w-]+)/update',views.UpdateAnswer.as_view(),name='update'),

]
