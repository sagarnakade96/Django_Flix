from django.db import models
from django.db.models.signals import pre_save
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.text import slugify

from Djangoflix.db.models import PublishedStateOptions
from Djangoflix.db.receivers import publish_state_pre_save, slugify_pre_save


class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(state=PublishedStateOptions.PUBLISH, publish_timestamp_lte=now)


class VideoManager(models.Manager):
    def get_querySet(self):
        return VideoQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=220)
    desc = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220, unique=True)
    active = models.BooleanField(default=True)
    state = models.CharField(
        max_length=2, choices=PublishedStateOptions.choices, default=PublishedStateOptions.DRAFT)
    publish_timestamp = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = VideoManager()

    @property
    def is_published(self):
        return self.active

    def get_playlist_ids(self):
        # self.<foreigned_obj>_set_all()
        return list(self.playlist_featured.all().values_list('id', flat=True))

    def save(self, *args, **kwargs):

        if self.slug is None:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'


class VideoNonpublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Non Published Video'
        verbose_name_plural = 'Non Published Videos'


pre_save.connect(publish_state_pre_save, sender=Video)


pre_save.connect(slugify_pre_save, sender=Video)
