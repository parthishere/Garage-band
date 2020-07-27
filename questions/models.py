from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.shortcuts import redirect
from portfolio.models import UserProfileModel,User

# Create your models here.
class Questions(models.Model):
    """ Question Model """
    question        = models.TextField()
    user            = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True)
    image           = models.ImageField(null=True,blank=True)
    slug            = models.SlugField(unique=True,blank=True,null=True)
    like            = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='liked_user')
    like_count      = models.IntegerField(default=0)
    dislike         = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='disliked_user')
    dislike_count   = models.IntegerField(default=0)
    time            = models.DateTimeField(null=True, blank=True)
        
    def __str__(self):
        """ str method """
        pk=self.pk
        return str(pk)

def questions_pre_save_receiver(sender,instance,*args,**kwargs):
    """ Signal """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(questions_pre_save_receiver,sender=Questions)


def user_pre_save_receiver(sender,instance,*args,**kwargs):
    """ Signal """
    request = kwargs.get("request")
    if not instance.user:
        instance.user = request.user
pre_save.connect(user_pre_save_receiver,sender=Questions)

