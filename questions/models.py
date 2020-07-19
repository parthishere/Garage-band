from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from portfolio.models import UserProfileModel
from django.urls import reverse

# Create your models here.
ALL_CHOICES = [
  ('VE','VIDEO EDITING'),
  ('PE','PHOTO EDITING'),
  ('C','COLORING'),
  ('V','VFX'),
  ('CG','CINEMETOGRAPHY'),
  ('W','WRITING'),
  ('CW','CONTENT WRITING'),
]

class Questions(models.Model):
    """ Question Model """
    question    = models.TextField(max_length=1000, help_text='Enter your question in brief')
    user        = models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
    image       = models.ImageField(null=True,blank=True)
    slug        = models.SlugField(unique=True,blank=True,null=True)
    time        = models.DateTimeField(auto_now_add=True)
    tag         = models.CharField(choices = ALL_CHOICES,max_length=3)


    def get_absolute_url(self):
        """Returns the url to access a particular question and its answer."""
        return reverse('question-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question_text}'

def questions_pre_save_receiver(sender,instance,*args,**kwargs):
    """ Signal """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(questions_pre_save_receiver,sender=Questions)
