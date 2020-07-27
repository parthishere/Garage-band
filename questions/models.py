from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.shortcuts import redirect
from portfolio.models import UserProfileModel,User

TAG_CHOICES = [
    ('EN', 'Entertainment'), 
    ('EN2', 'Entertaintment 2'),
    ('EN3', 'Entertaintment 3'),
    ('EN4', 'Entertaintment 4'),
    ('EN5', 'Entertaintment 5'),
]

# Create your models here.
class Questions(models.Model):
    """ Question Model """
    question    = models.TextField()
    user        = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True)
    image       = models.ImageField(null=True,blank=True)
    slug        = models.SlugField(unique=True,blank=True,null=True)
    like        = models.IntegerField(default=0)
    dislike     = models.IntegerField(default=0)
    time        = models.DateTimeField(auto_now_add=True)
    tags        = models.CharField(choices=TAG_CHOICES, max_length=3, default='EN')
        
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

