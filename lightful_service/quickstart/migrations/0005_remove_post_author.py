# Generated by Django 2.0.4 on 2018-04-23 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_post_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
