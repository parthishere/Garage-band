# Generated by Django 3.0.7 on 2020-07-21 07:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0030_auto_20200720_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 21, 7, 34, 41, 888271, tzinfo=utc), null=True),
        ),
    ]
