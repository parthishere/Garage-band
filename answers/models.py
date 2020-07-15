from django.db import models
from questions.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
from poertfolio.models import UserProfileModel

# Create your models here.
class Answers(models.Model):
    user = models.ForeignKey(UserProfileModel)
    answer = models.TextField(max_length=2000, help_text='Write your answer here...')
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    time =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'Que: {self.question.question_text[:50]}.. Ans: {self.answer_text[:50]}..'


def answers_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(answers_pre_save_receiver,sender=Answers)

class Comment(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=1000, help_text='Enter your comment...')
    time =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.comment_text}'
