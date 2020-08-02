from django.urls import path,re_path
from .views import AnswerDetailRudView,AnswerCreateAPIView

app_name = 'api-answers'
urlpatterns = [
    re_path('(?P<pk>\d+)/',AnswerDetailRudView.as_view(),name='answer-rud'),
    path('create/',AnswerCreateAPIView.as_view(),name='answer-create'),
]
