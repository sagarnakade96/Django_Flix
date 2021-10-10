# Generated by Django 3.2.4 on 2021-10-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('desc', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video_id', models.CharField(max_length=220, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('state', models.CharField(choices=[('PU', 'Published'), ('DR', 'Draft')], default='DR', max_length=2)),
                ('publish_timestamp', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
