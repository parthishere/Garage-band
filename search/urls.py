from django.urls import path, include
from .views import SearchView

app_name = 'search'

urlpatterns = [
   path('here/',SearchView.as_view(),name='search-here'),
   # path('auto/',autocomplete,name='auto')
]
