# Generated by Django 3.2.4 on 2021-10-10 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_alter_video_video_id'),
        ('playlist', '0003_auto_20211009_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playlist_featured', to='videos.video'),
        ),
    ]
