from django.contrib import admin
from .models import Announcement, Advertisement, Notice, Version, Event


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title']


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title']


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title']


class VersionAdmin(admin.ModelAdmin):
    list_display = ['title']


class EventAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Event, EventAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Announcement, AdvertisementAdmin)
