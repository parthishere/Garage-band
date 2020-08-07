from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from .models import UserProfileModel
# Register your models here.



# class UserLocation(OSMGeoAdmin):
#     list_display = ('name', 'location')


from django.conf.urls import url
from django.contrib import admin


admin.site.register(UserProfileModel)

admin.site.site_header = 'Garage-band admin'
admin.site.site_title = 'Garage-band admin'
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'Garage-band administration'