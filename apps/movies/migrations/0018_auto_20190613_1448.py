# Generated by Django 2.2 on 2019-06-13 14:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
