# Generated by Django 3.2.5 on 2022-08-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=256)),
                ('current_weight', models.IntegerField()),
                ('goal_weight', models.IntegerField()),
                ('rep_count', models.IntegerField()),
            ],
        ),
    ]