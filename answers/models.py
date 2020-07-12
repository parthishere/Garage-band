from django.db import models
from questions.utils import unique_slug_generator
from django.db.models.signals import pre_save

from poertfolio.models import UserProfileModel

# Create your models here.
class Answers(models.Model):
    user = models.OneToOneField(UserProfileModel)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    question_id = models.IntegerField(blank=True, null=True)
    like = models.IntegerField()
    time =models.DateTimeField(auto_now_add=True)

    def is_liked(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            self.like += 1
            self.save(using=self._db)
        else:
            return redirect('')


    def __str__(self,pk):
        pk=self.pk
        return pk

def answers_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(answers_pre_save_receiver,sender=Answers)

class Comment(models.Model):
    comment = models.TextField()
    like = models.IntegerField()
    time =models.DateTimeField(auto_now_add=True)

    def is_liked(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            self.like += 1
            self.save(using=self._db)
        else:
            return redirect('')
        return
