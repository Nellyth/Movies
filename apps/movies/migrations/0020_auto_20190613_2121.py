# Generated by Django 2.2 on 2019-06-13 21:21

import apps.movies.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_auto_20190613_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to=apps.movies.models.movie_directory_path),
        ),
    ]
