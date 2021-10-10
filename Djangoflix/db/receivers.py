from django.db.models.signals import pre_save
from django.utils import timezone
from .models import PublishedStateOptions
from django.utils.text import slugify


def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishedStateOptions.PUBLISH
    is_draft = instance.state == instance.VideoStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()

    elif is_draft:
        instance.publish.timestamp = None


def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)
