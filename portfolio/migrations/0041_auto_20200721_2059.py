# Generated by Django 3.0.7 on 2020-07-21 15:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0040_auto_20200721_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='followers',
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 21, 15, 29, 19, 580396, tzinfo=utc), null=True),
        ),
    ]