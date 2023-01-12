# Generated by Django 3.2.16 on 2023-01-10 20:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0004_auto_20230105_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='collabarators',
            field=models.ManyToManyField(blank=True, related_name='collabarator_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='forkers',
            field=models.ManyToManyField(blank=True, related_name='fork_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='star_givers',
            field=models.ManyToManyField(blank=True, related_name='star_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
