# Generated by Django 2.2.6 on 2020-07-27 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0047_auto_20200727_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 27, 13, 21, 42, 690856, tzinfo=utc), null=True),
        ),
    ]
