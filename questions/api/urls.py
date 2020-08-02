from django.urls import path,re_path
from .views import QuestionDetailRudView,QuestionCreateAPIView,QuestionListAPIView,QuestionDraftListAPIView,QuestionSavedListAPIView

app_name = 'api-questions'
urlpatterns = [
    re_path('(?P<pk>\d+)/',QuestionDetailRudView.as_view(),name='question-rud'),
    path('create/',QuestionCreateAPIView.as_view(),name='question-create'),
    path('list',QuestionListAPIView.as_view(),name='question-list'),
    # path('like',upvote_create_api_view,name='like')
    path('draft',QuestionDraftListAPIView.as_view(),name='question-draft'),
    path('saved',QuestionSavedListAPIView.as_view(),name='question-saved')
]
