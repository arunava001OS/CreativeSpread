# Generated by Django 3.0.1 on 2020-01-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativewriting', '0010_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
