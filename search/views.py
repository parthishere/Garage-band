from django.shortcuts import render
from django.views.generic import ListView
from questions.models import Questions
from portfolio.models import UserProfileModel
from itertools import chain
import json
from django.http import HttpResponse

class SearchView(ListView):
    template_name = 'search/search.html'
    paginate_by = 1
    count = 0
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q',None)
        if query is not None:
            question_results = Questions.objects.search(query=query)
            portfolio_results = UserProfileModel.objects.search(query=query)

            queryset_chain = chain(
            question_results,
            portfolio_results
            )
            qs = sorted(queryset_chain,key=lambda instance:instance.pk,reverse = True)
            self.count = len(qs)
            return qs
        return UserProfileModel.objects.none()
 # Create your views here.
# def autocomplete(request):
#     query_term = request.GET.get('term','')
#     question_result = Questions.objects.filter(title__contains=query_term)
#     # portfolio_result = UserProfileModel.objects.filter(user__username__icontains=query_term)
#
#     results = []
#     for result in question_result:
#         results.append(result.title)
#         # results.append(result.user)
#     data = json.dumps(results)
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)
