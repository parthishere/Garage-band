# Generated by Django 3.0.7 on 2020-07-17 04:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20200715_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 17, 4, 29, 11, 286878, tzinfo=utc), null=True),
        ),
    ]