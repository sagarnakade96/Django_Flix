# Generated by Django 3.2.4 on 2021-10-07 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20211006_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoNonpublishedProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Non Published Video',
                'verbose_name_plural': 'Non Published Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
