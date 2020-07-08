from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import User

from .validators import validate_image_file_extension, validate_music_file_extension, validate_video_file_extension


class UserProfileModel(models.Model):
    """ User Profile Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    phone_no = models.PhoneNumberField(unique=True)
    profession = models.TextField(max_length=100)
    Softwear = models.TextField(max_length=100)
    about = models.TextField(max_length=500)
    image = models.ImageField(upload_to='profiles')
    photography = models.ImageField(upload_to='work_photos', validators=[validate_image_file_extension])
    music = models.FileField(upload_to='work_musik'  ,validators=[validate_music_file_extension])
    video = models.FileField(upload_to='work_musik'  ,validators=[validate_video_file_extension])
    


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

