# Generated by Django 3.0.7 on 2020-07-17 05:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_auto_20200717_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 17, 5, 56, 22, 34311, tzinfo=utc), null=True),
        ),
    ]