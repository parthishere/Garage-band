# Generated by Django 3.0.7 on 2020-07-10 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200710_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 10, 20, 58, 25, 459885, tzinfo=utc), null=True),
        ),
    ]