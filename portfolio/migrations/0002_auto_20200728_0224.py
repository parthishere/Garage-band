# Generated by Django 3.0.7 on 2020-07-27 20:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 27, 20, 54, 50, 846054, tzinfo=utc), null=True),
        ),
    ]