# Generated by Django 3.0.7 on 2020-07-17 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_auto_20200717_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='tags',
            field=models.CharField(choices=[('EN', 'Entertainment')], default='EN', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 17, 6, 58, 23, 880882, tzinfo=utc), null=True),
        ),
    ]