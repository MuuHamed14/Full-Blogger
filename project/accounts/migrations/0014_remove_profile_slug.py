# Generated by Django 3.1 on 2020-10-03 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]