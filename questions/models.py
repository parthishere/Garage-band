from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class Questions(models.Model):
    question = models.TextField()
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    like = models.NumericField()
    time =models.DateTimeField(auto_now_add=True)

    def is_liked(self,*args,**kwargs,request):
        if request.user is authenticated:
            self.like += 1
            self.save(using=self._db)
        else:
            return redirect('')
        return

    def __str__(self,pk):
        pk=self.pk
        return pk

def questions_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(questions_pre_save_receiver,sender=Questions)
