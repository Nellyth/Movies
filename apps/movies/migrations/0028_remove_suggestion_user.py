# Generated by Django 2.2 on 2019-06-28 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0027_suggestion_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='user',
        ),
    ]
