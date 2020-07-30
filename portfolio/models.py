from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import User
from django.shortcuts import reverse, redirect
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# from django.contrib.gis.db import models


from .validators import validate_image_file_extension, validate_music_file_extension, validate_video_file_extension
from .utils import random_string_generator


TAG_CHOICES = [
    ('EN', 'Entertainment'), 
    ('EN2', 'Entertaintment 2'),
    ('EN3', 'Entertaintment 3'),
    ('EN4', 'Entertaintment 4'),
    ('EN5', 'Entertaintment 5'),
]



def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.user.username)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug



class UserProfileManager(models.Manager):
    """ User profile manager """
    def create_or_get(self, request, user, email, password):
        """ creating user or getting user """
        new_obj = False
        u = request.session.get['user']
        query = self.model.get(user=user)
        if query.count()==1 and query.exist():
            return query.first()
        else:
            user = UserProfileModel(user=user, email=email)
            user.set_password(password)
            user.save()
            new_obj=True
            self.request.session['user'] = user.id  
            return user, new_obj      


        


class UserProfileModel(models.Model):
    """ User Profile Model """
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    dob             = models.DateField(null=True, blank=True, default=timezone.now())
    phone_no        = PhoneNumberField(null=True, blank=True)
    profession      = models.TextField(max_length=100, null=True, blank=True)
    softwear        = models.TextField(max_length=100,null=True, blank=True)
    about           = models.TextField(max_length=500,null=True, blank=True)
    image           = models.ImageField(upload_to='profiles/', null=True, blank=True)
    photography     = models.ImageField(upload_to='work_photos/', validators=[validate_image_file_extension],null=True, blank=True)
    music           = models.FileField(upload_to='work_music/'  ,validators=[validate_music_file_extension],null=True, blank=True)
    video           = models.FileField(upload_to='work_video/'  ,validators=[validate_video_file_extension],null=True, blank=True)
    awards          = models.TextField(null=True, blank=True)
    slug            = models.SlugField(null=True, blank=True)
    tags            = models.CharField(choices=TAG_CHOICES, default='EN', max_length=3)
    

    objects = UserProfileManager()

    

    def __str__(self):
        ''' Representation of instances '''
        return str(f"email:{self.user.email}  id: {self.pk}")

    def get_absolute_url(self):
        """ Url methodes """
        return reverse('portfolio:detail', kwargs={'slug':self.slug})
    
    def get_featured_profile(self):
        return UserProfileModel.objects.first()



def product_pre_save_receiver(sender, instance, *args, **kwargs):
    """ slug genrator signal """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=UserProfileModel)
    


def user_post_save_reciever(sender, instance, created, *args, **kwargs):
    if created:
        UserProfileModel.objects.get_or_create(user=instance)

post_save.connect(user_post_save_reciever, sender=User)
