# Generated by Django 4.0 on 2022-10-24 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
