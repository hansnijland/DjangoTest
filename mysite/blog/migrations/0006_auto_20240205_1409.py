# Generated by Django 3.2.23 on 2024-02-05 13:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_rename_dureparadepaardjes_dureparadepaardje'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voetbalspelers',
            new_name='Voetbalspeler',
        ),
        migrations.DeleteModel(
            name='Dureparadepaardje',
        ),
    ]
