import graphene
from graphene_django.types import DjangoObjectType
from .models import Advertisement, Announcement, Notice, Version, Event


class AdvertisementType(DjangoObjectType):
    class Meta:
        model = Advertisement


class AnnouncementType(DjangoObjectType):
    class Meta:
        model = Announcement


class NoticeType(DjangoObjectType):
    class Meta:
        model = Notice


class VersionType(DjangoObjectType):
    class Meta:
        model = Version


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class Query(graphene.AbstractType):
    all_event = graphene.List(EventType)

    all_version = graphene.List(VersionType)

    all_advertisement = graphene.List(AdvertisementType)

    all_announcement = graphene.List(AdvertisementType)

    all_notice = graphene.List(NoticeType)

    def resolve_all_event(self, context, **kwargs):
        return Event.objects.all()

    def resolve_all_version(self, context, **kwargs):
        return Version.objects.all()

    def resolve_all_notice(self, context, **kwargs):
        return Notice.objects.all()

    def resolve_all_advertisement(self, context, **kwargs):
        return Advertisement.objects.all()

    def resolve_all_announcement(self, context, **kwargs):
        return Advertisement.objects.all()