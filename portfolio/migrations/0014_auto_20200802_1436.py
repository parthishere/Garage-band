# Generated by Django 3.0.3 on 2020-08-02 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20200802_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 2, 9, 5, 59, 305011, tzinfo=utc), null=True),
        ),
    ]
