# Generated by Django 2.2 on 2019-06-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0025_movie_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
