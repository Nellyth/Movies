# Generated by Django 2.2 on 2019-06-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_auto_20190613_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
