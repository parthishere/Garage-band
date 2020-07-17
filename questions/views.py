from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import QuestionForm
from .models import Questions
from answers.models import Answers
from portfolio.models import UserProfileModel
from answers.forms import PostAnswerForm 


# Create your views here.


class QuestionCreate(LoginRequiredMixin, FormView):
    form_class = QuestionForm
    template_name = 'questions/ask-question.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.user = request.user
        # instance_user = UserProfileModel.objects.get(user=request.user)
        # form.instance.user = request.user
        if form.is_valid():
            form.save()
            return reverse('questions:question-list')
        else:
            return reverse('questions:question-detail')

    # def get_success_url(self):
    #     return reverse_lazy('questions:question-list')


class QuestionListView(ListView):
    model = Questions
    template_name = 'questions/question-list.html'
    
    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['objects_list'] = Questions.objects.all()
        return context


class QuestionDetailView(DetailView, FormView):
    template_name = 'questions/question-detail.html'
    model = Questions
    form_class = PostAnswerForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None: 
            pk = request.GET.get('pk')  
        form = self.form_class(request.POST)
        form.instance.question_id = request.GET.get('pk')
        # instance_user = UserProfileModel.objects.get(user=request.user)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return reverse('questions:question-detail', kwargs={'pk': pk})
        else:
            return reverse('questions:question-detail', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['answers'] = Answers.objects.filter(question_id=pk)
        return context
        # else:
        #     raise AttributeError("pk not found in url")
    