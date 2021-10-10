# Generated by Django 3.2.4 on 2021-10-09 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_alter_video_video_id'),
        ('playlist', '0002_auto_20211009_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, related_name='playlist_item', to='videos.Video'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.video'),
        ),
    ]
