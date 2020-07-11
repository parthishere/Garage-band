from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from questions import views

app_name = 'answers'

urlpatterns = [
    path('',views.questions,name='question'),
    path('ask/',views.ask_question_view,name='ask'),

]
