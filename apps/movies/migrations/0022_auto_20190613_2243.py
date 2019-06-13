# Generated by Django 2.2 on 2019-06-13 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_auto_20190613_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='movieactor',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
