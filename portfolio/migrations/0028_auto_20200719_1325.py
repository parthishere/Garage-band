# Generated by Django 3.0.7 on 2020-07-19 07:55

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0027_auto_20200717_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers_of_instance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 19, 7, 55, 47, 973685, tzinfo=utc), null=True),
        ),
    ]