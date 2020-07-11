from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from questions.models import Questions
from portfolio.models import UserProfileModel
# Create your views here.
class QuestionSearchView(ListView):
    template_name = 'search/search_view.html'

    

    def get_queryset(self,*args,**kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q')
        if query is not None:
            lookups = Q(question__icontains=query) | Q(user__icontains=query) | Q(image__icontains=query)
            return Questions.objects.filter(lookups)
        return Questions.objects.none()
