# Generated by Django 3.0.1 on 2019-12-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativewriting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='num_articles',
            field=models.IntegerField(default=0),
        ),
    ]
