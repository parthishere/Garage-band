from django.shortcuts import render, redirect, reverse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView, DetailView, FormView, DeleteView, UpdateView
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import QuestionForm
from .models import Questions
from answers.models import Answers
from portfolio.models import UserProfileModel
from answers.forms import PostAnswerForm 


# Create your views here.



class AnswerDetailView(DetailView, FormView):
    template_name = 'answer/answer-detail.html'
    model = Questions
    form_class = PostAnswerForm

    def get_context_data(self, *args, **kwargs):
        pk = kwargs.get('pk') 
        context = super(QuestionDetailView, self).get_context_data(*args, **kwargs)
        context['form'] = self.get_form()
        question = Questions.objects.get(pk=pk)
        context['answers'] = Answers.objects.filter(question=question)
        context['object'] = Question.objects.get(pk=pk)
        print(context['answers'])
        
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        pk = request.GET.get('pk')
        pk = kwargs.get('pk')
        if pk:
            question = Questions.objects.get(pk=pk)
            answers = Answers.objects.filter(question=question)
            obj = Questions.objects.get(pk=pk)
            context = {
                'form':form,
                'answers': answers,
                'object':obj
            }
            return render(request, self.template_name, context)
        else:
            return HttpResponse("Something gone wrong")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None: 
            pk = request.GET.get('pk')  
        form = self.form_class(request.POST)
        question = Questions.objects.get(pk=pk)
        form.instance.question = question
        form.instance.user = request.user
        print(object)
        if form.is_valid():
            form.save()
            return redirect(reverse('questions:detail', kwargs={'pk': pk}))
        else:
            return redirect(reverse('questions:detail', kwargs={'pk': pk}))
  


class AnswerDeleteView(DeleteView):
    model = Questions
    success_url = reverse_lazy('questions:list')
    template_name_suffix = '_confirm_delete'

class AnswerUpdateView(UpdateView):
    model = Questions
    fields = ['question', 'image']
    template_name_suffix = '_update_form'
    
