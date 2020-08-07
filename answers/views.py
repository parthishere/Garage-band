from django.shortcuts import render, redirect, reverse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView, DetailView, FormView, DeleteView, UpdateView
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from answers.models import Answers, Comment
from portfolio.models import UserProfileModel
from answers.forms import PostAnswerForm, PostCommentForm 


# Create your views here.



class AnswerDetailView(DetailView, FormView):
    template_name = 'answers/answer-detail.html'
    model = Answers
    form_class = PostCommentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        pk = kwargs.get('pk')
        if pk is None: 
            pk = request.GET.get('pk')
        if pk:
            answer = Answers.objects.get(pk=pk)
            comment = Comment.objects.filter(answer=answer)
            obj = Answers.objects.get(pk=pk)
            context = {
                'form':form,
                'comments': comment,
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
        answer = Answers.objects.get(pk=pk)
        form.instance.answer = answer
        form.instance.user = request.user
        print(object)
        if form.is_valid():
            form.save()
            return redirect(reverse('answers:detail', kwargs={'pk': pk}))
        else:
            return redirect(reverse('answers:detail', kwargs={'pk': pk}))
  


class AnswerDeleteView(DeleteView, LoginRequiredMixin):
    model = Answers
    success_url = reverse_lazy('questions:list')
    template_name_suffix = '_confirm_delete'

class AnswerUpdateView(UpdateView, LoginRequiredMixin):
    model = Answers
    fields = ['answer', 'image']
    template_name_suffix = '_update_form'
    
    def get_success_url(self, *kwargs):
        return reverse_lazy('answers:detail', kwargs = {'pk': self.object.pk})
    
