# Generated by Django 5.0.3 on 2024-03-17 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_video_rename_image_news_attached_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='video',
            new_name='attached_video',
        ),
    ]
