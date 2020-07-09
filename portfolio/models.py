from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# from django.contrib.gis.db import models


from .validators import validate_image_file_extension, validate_music_file_extension, validate_video_file_extension
from .utils import random_string_generator



def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

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
    """ USer profile manager """
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
    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    followers   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_user' ,null=True, blank=True)
    dob         = models.DateField(null=True, blank=True, default=datetime.datetime.now())
    phone_no    = PhoneNumberField(null=True, blank=True)
    profession  = models.TextField(max_length=100, null=True, blank=True)
    softwear    = models.TextField(max_length=100,null=True, blank=True)
    about       = models.TextField(max_length=500,null=True, blank=True)
    image       = models.ImageField(upload_to='profiles/',null=True, blank=True)
    photography = models.ImageField(upload_to='work_photos/', validators=[validate_image_file_extension],null=True, blank=True)
    music       = models.FileField(upload_to='work_music/'  ,validators=[validate_music_file_extension],null=True, blank=True)
    video       = models.FileField(upload_to='work_video/'  ,validators=[validate_video_file_extension],null=True, blank=True)
    awards      = models.TextField(null=True, blank=True)
    slug        = models.SlugField(null=True, blank=True)
    # location = models.PointField()


    objects = UserProfileManager()

    def __str__(self):
        ''' Representation of instances '''
        return self.user.username

    def get_absolute_url(self):
        """ Url methodes """
        return reverse('/')



def product_pre_save_receiver(sender, instance, *args, **kwargs):
    """ slug genrator signal """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=UserProfileModel)
    


# Create your models here.
# class UserProfileManager(BaseUserManager):
#     """ User profile manager """

#     def create_user(self, email, password, date_of_birth, username):
#         """ function for creation users """
#         if not email:
#             raise ValueError("Somthing is Wrong With Email !")
#         user_instance = self.model(
#             email=UserProfileManager.normalize_email(email),
#             date_of_birth=date_of_birth,
#             username=username,
#         )
#         user_instance.set_password(password)
#         user_instance.save(using=self._db)
#         return user_instance
    
#     def create_superuser(self, email, password, date_of_birth, username):
#         if not email:
#             raise ValueError("Somthing is Wrong With Email !")
#         user_instance = self.model(
#             email=UserProfileManager.normalize_email(email),
#             date_of_birth=date_of_birth,
#             username=username,
#         )
#         user_instance.set_password(password)
#         user_instance.is_admin = True
#         user_instance.is_staff = True
#         user_instance.save(using=self._db)
#         return user_instance


# class UserProfileModel(AbstractBaseUser):
#     """ User Profile Model """
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True
#         )
#     username = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserProfileManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = ('username',)

#     def get_full_name(self):
#         """ Get Full Name """
#         return self.username
    
#     def __str__(self):
#         return f'email = {self.email}  username = {self.username}'

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.is_admin

