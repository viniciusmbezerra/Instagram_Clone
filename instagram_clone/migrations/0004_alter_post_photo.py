# Generated by Django 4.0 on 2022-10-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_clone', '0003_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='instagram_clone/post_photos/'),
        ),
    ]
