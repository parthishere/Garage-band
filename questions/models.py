from django.db import models
from django.utils import timezone
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.shortcuts import redirect, reverse
from portfolio.models import User
import tags.models
from ckeditor.fields import RichTextField
from django.db.models import Q
class QuestionQuerySet(models.QuerySet):
    def search(self,query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(title__icontains=query)|
                        Q(question__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs




class QuestionManager(models.Manager):
    def draft(self):
        return self.model.objects.filter(draft=False)

    def all_tags(self):
        return self.tags.tag_name

    def get_queryset(self):
        return QuestionQuerySet(self.model,using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

# Create your models here.
class Questions(models.Model):
    """ Question Model """
    # question        = models.TextField()
    title           = models.CharField(max_length=150)
    question        = RichTextField(config_name='default')
    user            = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True)
    image           = models.ImageField(null=True,blank=True)
    slug            = models.SlugField(unique=True,blank=True,null=True)
    like            = models.ManyToManyField(User, blank=True, related_name='liked_user')
    dislike         = models.ManyToManyField(User, blank=True, related_name='disliked_user')
    like_count      = models.IntegerField(default=0)
    dislike_count   = models.IntegerField(default=0)
    time            = models.DateTimeField(auto_now_add=True)
    tags            = models.ManyToManyField(tags.models.Tag, blank=True)
    draft           = models.BooleanField(default=False)
    # saved           = models.BooleanField(default=False)
    saved           = models.ManyToManyField(User, blank=True, related_name='lsaved_by_user')

    objects = QuestionManager()

    class Meta:
        ordering = [ '-time' ]

    def __str__(self):
        """ str method """
        return str(f"{self.question} by {self.user}")

    def get_absolute_url(self):
        return reverse("questions:detail", kwargs={"pk": self.pk})



# class SavedQuestion(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

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
