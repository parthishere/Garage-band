# Generated by Django 3.0.7 on 2020-07-21 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0038_auto_20200721_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 21, 14, 2, 48, 894554, tzinfo=utc), null=True),
        ),
    ]
