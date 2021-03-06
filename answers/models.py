from django.db import models
from questions.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.shortcuts import reverse, redirect

import questions.models 
from portfolio.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class AnswersManager(models.Manager):

    def upvote_create(self, q_pk):
        answer_instance = self.instance
        answer_instance.like += 1
        answer_instance.save()
        return reverse('question:detail', kwargs={'pk':q_pk})

    def downvote_create(self, q_pk):
        answer_instance = self.instance
        answer_instance.dislike += 1
        answer_instance.save()
        return reverse('question:detail', kwargs={'pk':q_pk})



class Answers(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True ,null=True)
    image           = models.ImageField(null=True,blank=True)
    answer          = RichTextField(blank=True, null=True, config_name='default')
    slug            = models.SlugField(unique=True,blank=True,null=True)
    question        = models.ForeignKey(questions.models.Questions, on_delete=models.CASCADE, blank=True ,null=True)
    like            = models.ManyToManyField(User, blank=True, related_name='answer_iked_user')
    dislike         = models.ManyToManyField(User, blank=True, related_name='answer_disliked_user')
    like_count      = models.IntegerField(default=0)
    dislike_count   = models.IntegerField(default=0)
    time            = models.DateTimeField(auto_now_add=True)
    parant          = models.BooleanField(default=True)

    objects = AnswersManager()

    class Meta:
        ordering = [ '-time' ]

    def __str__(self):
        pk=self.pk
        return str(pk)  

    def get_absolute_url(self):
        return reverse("answers:detail", kwargs={"pk": self.pk})
    
     



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, blank=True, null=True)
    time    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ '-time' ]

    def __str__(self):
        return str(self.pk)


def user_pre_save_receiver(sender,instance,*args,**kwargs):
    """ Signal """
    request = kwargs.get('request')
    if not instance.user:
        instance.user = request.user
pre_save.connect(user_pre_save_receiver,sender=Answers)