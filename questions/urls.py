from django.urls import path

from . import views
app_name = 'question'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='questions'),
	path('question/add/', views.QuestionCreate.as_view(), name='question-add'),
    path('question/<slug>', views.QuestionDetailView.as_view(), name='question-detail'),

]
