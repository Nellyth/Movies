# Generated by Django 2.2 on 2019-06-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20190607_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieactor',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
