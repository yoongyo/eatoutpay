import graphene
from graphene_django.types import DjangoObjectType

from .models import RestaurantCategory, Restaurant, MenuCategory, Menu


class RestaurantCategoryType(DjangoObjectType):
    class Meta:
        model = RestaurantCategory


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant


class MenuCategoryType(DjangoObjectType):
    class Meta:
        model = MenuCategory


class MenuType(DjangoObjectType):
    class Meta:
        model = Menu


class Query(graphene.AbstractType):
    all_restaurantCategory = graphene.List(RestaurantCategoryType)
    all_restaurant = graphene.List(RestaurantType)
    all_menuCategory = graphene.List(MenuCategoryType)
    all_menu = graphene.List(MenuType)

    def resolve_all_restaurantCategory(self, context, **kwargs):
        return RestaurantCategory.objects.all()

    def resolve_all_restaurant(self, context, **kwargs):
        return Restaurant.objects.all()

    def resolve_all_menuCategory(self, context, **kwargs):
        return MenuCategory.objects.all()

    def resolve_all_menu(self, context, **kwargs):
        return Menu.objects.all()