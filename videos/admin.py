from django.contrib import admin

from .models import VideoAllProxy, VideoPublishedProxy, VideoNonpublishedProxy

# Register your models here.


# class VideoAdmin(admin.ModelAdmin):
#     list_display = ['id','title','video_id']
#     search_fields = ['title']
#     # list_filter = ['video_id']
#     class Meta:
#         model = Video

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'video_id', 'is_published',
                    'publish_timestamp', 'get_playlist_ids']
    search_fields = ['title']
    list_filter = ['video_id', 'publish_timestamp']
    readonly_fields = ['id', 'is_published']

    class Meta:
        model = VideoAllProxy


admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'video_id']
    search_fields = ['title']
    # list_filter = ['video_id']

    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoAllProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)

# class VideoNonPublishedProxyAdmin(admin.ModelAdmin):
#     list_display = ['id','title','video_id']
#     search_fields = ['title']
#     # list_filter = ['video_id']
#     class Meta:
#         model = VideoNonpublishedProxy
#     def get_queryset(self,request):
#         return VideoAllProxy.objects.filter(active = False)

# admin.site.register(VideoNonpublishedProxy,VideoNonPublishedProxyAdmin)


# class videoProxyAdmin()
