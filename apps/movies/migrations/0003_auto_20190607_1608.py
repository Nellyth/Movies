# Generated by Django 2.2 on 2019-06-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190607_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movies.MovieActor'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(to='movies.MovieDirector'),
        ),
    ]
