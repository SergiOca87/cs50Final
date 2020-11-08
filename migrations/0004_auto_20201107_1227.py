# Generated by Django 3.1 on 2020-11-07 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectplanner', '0003_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='admin',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='notifications',
            field=models.BooleanField(blank=True, default=None, help_text='If enabled, users related to this project will get e-mail notifications.', null=True),
        ),
    ]