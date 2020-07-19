from django.urls import path,re_path

from . import views
app_name = 'question'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='questions'),
	path('question/add/', views.QuestionCreate.as_view(), name='question-add'),
    re_path('question/(?P<slug>[\w-]+)', views.QuestionDetailView.as_view(), name='question-detail'),
    re_path('/(?P<slug>[\w-]+)/delete',views.QuestionDelete.as_view(),name='delete'),
    re_path('/(?P<slug>[\w-]+)/update',views.UpdateQuestion.as_view(),name='update'),


]
