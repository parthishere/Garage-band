# Generated by Django 3.0.7 on 2020-07-21 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0033_auto_20200721_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 21, 13, 38, 7, 937741, tzinfo=utc), null=True),
        ),
    ]
