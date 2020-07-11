from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views
from questions.views import QuestionDetailSlugView

app_name = 'search'

urlpatterns = [

    path('',views.QuestionSearchView.as_view(),name='query'),
    re_path('(?P<slug>[\w-]+)/',QuestionDetailSlugView.as_view(),name='detail'),
]
