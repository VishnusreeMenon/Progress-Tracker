# Generated by Django 3.2.5 on 2022-09-04 05:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_progress', '0002_addexercise_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddExercise',
            new_name='Exercise',
        ),
    ]