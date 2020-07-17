from django.db import models
from questions.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.shortcuts import reverse, redirect
from portfolio.models import UserProfileModel, User

# Create your models here.
class Answers(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True ,null=True)
    image       = models.ImageField(null=True,blank=True)
    answer      = models.TextField(default='Enter Your Answer Here!')
    slug        = models.SlugField(unique=True,blank=True,null=True)
    question_id = models.IntegerField(blank=True, null=True)
    like        = models.IntegerField()
    time        =models.DateTimeField(auto_now_add=True)

    def is_liked(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            self.like += 1
            self.save(using=self._db)
        else:
            return redirect('portfolio:home')


    def __str__(self):
        pk=self.pk
        return str(pk)

# def answers_pre_save_receiver(sender,instance,*args,**kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
# pre_save.connect(answers_pre_save_receiver,sender=Answers)

class Comment(models.Model):
    comment = models.TextField()
    like    = models.IntegerField()
    time    = models.DateTimeField(auto_now_add=True)

    def is_liked(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            self.like += 1
            self.save(using=self._db)
        else:
            return redirect('')
        return


def user_pre_save_receiver(sender,instance,*args,**kwargs):
    """ Signal """
    request = kwargs.get('request')
    if not instance.user:
        instance.user = request.user
pre_save.connect(user_pre_save_receiver,sender=Answers)
