from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from myquora.models import Answer, Author, Comment, Question


class CommentCreate(LoginRequiredMixin, CreateView):
    form = CommentForm

    def get(self, request, *args, **kwargs):
        answer_id = self.kwargs['pk']
        return render(request, 'answers/comment-form.html', {"answer_id": answer_id})

    def post(self, request, *args, **kwargs):
        comment = request.POST.get('comment')
        params = self.kwargs['pk']
        user = UserProfileModel.objects.get(user=self.request.user)
        answer = Answer.objects.get(id=params)
        Comment.objects.create(
            user=user, answer=answer, comment=comment)
        response = redirect(
            reverse('question-detail', kwargs={'pk': answer.question.id}))
        return response


class UpvoteCreate(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer', 'answer_id', 'upvote']

    def post(self, request, *args, **kwargs):
        answer_id = self.kwargs['slug']
        answer = Answer.objects.get(id=answer_id)
        answer.upvote += 1
        answer.save()
        response = redirect(
            reverse('question-detail', kwargs={'pk': answer.question.id}))
        return response


class DownvoteCreate(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer', 'answer_id', 'downvote']

    def post(self, request, *args, **kwargs):
        answer_id = self.kwargs['slug']
        answer = Answers.objects.get(id=answer_id)
        answer.downvote += 1
        answer.save()
        response = redirect(
            reverse('question-detail', kwargs={'slug': answer.question_id.id}))
        return response

class AnswerCreate(LoginRequiredMixin, CreateView):
    form_class = AnswerForm
    template_name = answers/post-answer.html

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        form.instance.answer_id = request.GET.get('answer_id')
        if form.is_valid():
            form.save()
            return redirect(reverse('answer:answers'))

class AnswerListView(generic.ListView):
    model = Answer
    paginate_by = 3
