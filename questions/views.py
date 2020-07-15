from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, View ,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QuestionForm
from answers.forms import PostAnswerForm

# Create your views here.
class QuestionCreate(LoginRequiredMixin, CreateView):
    model = QuestionForm
    exclude = ['user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def question_detail_view(request, slug):
	question = Questions.objects.get(slug=slug)
	question_id = question.pk
	ans_form = PostAnswerForm(request.POST or None)
	ans_form.cleaned_data.get(question_id) = question_id
	if request.POST:
		if ans_form.is_valid():
			ans_form.save()
			return redirect('question-detail' slug=slug)

def QuestionDetailView(View):
	template_name = 'question-detail.html'
	form_class = PostAnswerForm

	def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        form.instance.question_id = request.GET.get('question_id')
        if form.is_valid():
            form.save()
            return redirect(reverse('question:questions'))

    def get_context_data(self, *args, **kwargs):
    	super().get_context_data(*args, **kwargs)
        question_id = self.kwargs['slug']
        question = Question.objects.get(id=question_id)
        answer_list = Answer.objects.filter(question=question)
        comment_dictionary = {
                ans.id: Comment.objects.filter(answer=ans) for ans in answer_list
            }
        context['answer_list'] = answer_list
        context['answer_url'] = '/question/'+str(question_id)+'/answer/'
        context['upvote_url'] = '/answer/upvote/'
        context['downvote_url'] = '/answer/downvote/'
        context['comment_dictionary'] = comment_dictionary
        return context

class QuestionListView(generic.ListView):
        model = Questions
        paginate_by = 10
