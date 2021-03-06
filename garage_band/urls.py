"""garage_band URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('portfolio.urls', namespace='portfolio')),
    path('friendship/', include('friendship.urls')),
    path('question/', include('questions.urls', namespace='questions')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/profile/', include('portfolio.api.urls', namespace='portfolio-api')),
    path('api/question/', include('questions.api.urls', namespace='question-api')),
    path('api/answer/', include('answers.api.urls', namespace='answers-api')),
    path('answers/', include('answers.urls', namespace='answers')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search/',include('search.urls',namespace='search'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
