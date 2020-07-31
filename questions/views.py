from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView, DetailView, FormView, DeleteView, UpdateView
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .forms import QuestionForm
from .models import Questions, SavedQuestion
from answers.models import Answers
from portfolio.models import UserProfileModel, User
from answers.forms import PostAnswerForm 
from friendship.models import Follow, Block, Friend

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
            return redirect(reverse('questions:list'))
        else:
            return redirect(reverse('questions:list'))

    # def get_success_url(self):
    #     return reverse_lazy('questions:question-list')


class QuestionListView(ListView):
    model = Questions
    template_name = 'questions/question-list.html'

    def get_context_data(self, **kwargs):
        request = self.request
        context = super(QuestionListView, self).get_context_data(**kwargs)
        list_of_following = Follow.objects.following(request.user)
        questions_following = Questions.objects.filter(user__in=[u for u in list_of_following]).filter(draft=False)
        user = UserProfileModel.objects.get(user=request.user)
        questions = Questions.objects.filter(tags__in=[tag for tag in user.tags]).filter(draft=False)
        context['objects_list'] = Questions.objects.filter(draft=False)
        context['questions_following'] = questions_following
        context['questions'] = questions
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
        


def search_question(request):
    query = request.GET.get('q')
    print(query)
    if query is not None:
        obj_list = (
                Q(question__icontains=query) | Q(tags__icontains=query) 
            )
        object_list = Questions.objects.filter(obj_list).distinct()
        context = {
            'object_list': object_list
        }
        return render(request, 'questions/search-question.html', context)
    else:
        return HttpResponse("Something gone wrong")

    #         
 



@login_required
def upvote_create(request, pk, q_pk):
    answer_instance = Answers.objects.get(pk=pk)
    if request.user in answer_instance.like.all():
        answer_instance.like.remove(request.user)
        if answer_instance.like_count>=0:
            answer_instance.like_count -= 1
        else:
            answer_instance.like_count = 0
        answer_instance.save()
    else:    
        # u1 = UserProfileModel.objects.get(user=request.user)
        answer_instance.like.add(request.user)
        if answer_instance.like_count>=0:
            answer_instance.like_count += 1
        else:
            answer_instance.like_count = 0
        answer_instance.save()
    return redirect(reverse('questions:detail', kwargs={'pk':q_pk}))


@login_required
def downvote_create(request, pk, q_pk):
    answer_instance = Answers.objects.get(pk=pk)
    if request.user in answer_instance.like.all():
        answer_instance.dislike.remove(request.user)
        if answer_instance.dislike_count>=0:
            answer_instance.dislike_count -= 1
        else:
            answer_instance.dislike_count = 0
        answer_instance.save()
    else:
        # u1 = User.objects.get(user=request.user)
        answer_instance.dislike.add(request.user)
        if answer_instance.dislike_count>=0:
            answer_instance.dislike_count += 1
        else:
            answer_instance.dislike_count = 0
    return redirect(reverse('questions:detail', kwargs={'pk':q_pk}))   


@login_required
def question_upvote_create(request, pk):
    question_instance = Questions.objects.get(pk=pk)
    if request.user in question_instance.like.all():
        question_instance.like.remove(request.user)
        if question_instance.like_count>=0:
            question_instance.like_count -= 1
        else:
            question_instance.like_count = 0
        question_instance.save()
    else:    
        # u1 = UserProfileModel.objects.get(user=request.user)
        question_instance.like.add(request.user)
        if question_instance.like_count>=0:
            question_instance.like_count += 1
        else:
            question_instance.like_count = 0
        question_instance.save()
    return redirect(reverse('questions:detail', kwargs={'pk':pk}))


@login_required
def question_downvote_create(request, pk):
    question_instance = Questions.objects.get(pk=pk)
    if request.user in question_instance.like.all():
        question_instance.dislike.remove(request.user)
        if question_instance.dislike_count>=0:
            question_instance.dislike_count -= 1
        else:
            question_instance.dislike_count = 0
        question_instance.save()
    else:
        # u1 = User.objects.get(user=request.user)
        question_instance.dislike.add(request.user)
        if question_instance.dislike_count>=0:
            question_instance.dislike_count += 1
        else:
            question_instance.dislike_count = 0
        question_instance.save()
    return redirect(reverse('questions:detail', kwargs={'pk':pk}))  
  


class QuestionDeleteView(DeleteView, LoginRequiredMixin):
    model = Questions
    success_url = reverse_lazy('questions:list')
    template_name_suffix = '_confirm_delete'
    
    

class QuestionUpdateView(UpdateView, LoginRequiredMixin):
    model = Questions
    fields = ['question', 'image']
    template_name_suffix = '_update_form'
    
def feed(request):
    list_of_following = Follow.objects.following(request.user)
    user = UserProfileModel.objects.get(user=request.user)
    questions = Questions.objects.filter(tags=[tag for tag in user.tags])
    return None


class QuestionDraftListView(ListView):
    model = Questions
    template_name = 'questions/draft-list.html'
    
    def get_context_data(self, **kwargs):
        request = self.request
        context = super(QuestionDraftListView, self).get_context_data(**kwargs)
        context["objects_list"] = Questions.objects.filter(user=request.user).filter(draft=True) 
        return context
    
    
class SavedQuestionListView(ListView):
    model = SavedQuestion
    template_name = 'questions/saved-questions.html'
    
    def get_context_data(self, **kwargs):
        request = self.request
        context = super(SavedQuestionListView, self).get_context_data(**kwargs)
        context["objects_list"] = SavedQuestion.objects.filter(user=request.user) 
        return context

@login_required
def save_question(request, pk):
    if request.user.is_authenticated:
        
        obj = get_object_or_404(Questions, pk=pk)
        if obj in SavedQuestion.objects.filter(user=request.user):
            return redirect(reverse('questions:detail', kwargs={'pk':pk}))
        else:
            saved_obj = SavedQuestion.objects.create(user=request.user, question=obj)
            return redirect(reverse('questions:detail', kwargs={'pk':pk}))
    else:
        return redirect(reverse('questions:detail', kwargs={'pk':pk}))
    
