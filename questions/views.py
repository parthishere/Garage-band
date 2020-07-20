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
            return reverse('questions:list')
        else:
            return reverse('questions:detail')

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

def upvote_create(self, pk, q_pk):
        answer_instance = Answers.objects.get(pk=pk)
        answer_instance.like += 1
        answer_instance.save()
        return redirect(reverse('questions:detail', kwargs={'pk':q_pk}))

def downvote_create(self, pk, q_pk):
    answer_instance = Answers.objects.get(pk=pk)
    answer_instance.dislike += 1
    answer_instance.save()
    return redirect(reverse('questions:detail', kwargs={'pk':q_pk}))   
  

# class UpvoteCreate(LoginRequiredMixin, CreateView):
#     model = Answers
#     fields = ['answer', 'like']

#     def post(self, request, *args, **kwargs):
#         answer_id = self.kwargs['pk']
#         answer = Answers.objects.get(id=answer_id)
#         answer.like += 1
#         answer.save()
#         response = redirect(
#             reverse('question:detail', kwargs={'pk': answer.question.id}))
#         return response


# class DownvoteCreate(LoginRequiredMixin, CreateView):
#     model = Answers
#     fields = ['answer', 'dislike']

#     def post(self, request, *args, **kwargs):
#         answer_id = self.kwargs['pk']
#         answer = Answers.objects.get(id=answer_id)
#         answer.dislike += 1
#         answer.save()
#         response = redirect(
#             reverse('question:detail', kwargs={'pk': answer.question.id}))
#         return response

class QuestionDeleteView(DeleteView):
    model = Questions
    success_url = reverse_lazy('questions:list')
    template_name_suffix = '_confirm_delete'

class QuestionUpdateView(UpdateView):
    model = Questions
    fields = ['question', 'image']
    template_name_suffix = '_update_form'
    
