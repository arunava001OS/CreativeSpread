# Generated by Django 3.0.1 on 2020-01-01 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creativewriting', '0008_auto_20200101_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
    ]
