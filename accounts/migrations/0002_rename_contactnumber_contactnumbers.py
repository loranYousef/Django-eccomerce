# Generated by Django 4.2 on 2023-11-25 07:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactNumber',
            new_name='ContactNumbers',
        ),
    ]
