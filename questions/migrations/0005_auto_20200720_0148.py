# Generated by Django 3.0.7 on 2020-07-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20200717_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]