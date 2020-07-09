from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from .models import UserProfileModel
# Register your models here.


admin.site.register(UserProfileModel)
# class UserLocation(OSMGeoAdmin):
#     list_display = ('name', 'location')