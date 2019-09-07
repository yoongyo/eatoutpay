import graphene
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from .models import RestaurantCategory, Restaurant, MenuCategory, Menu, Area


class AreaType(DjangoObjectType):
    class Meta:
        model = Area


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
    restaurant = graphene.Field(RestaurantType,
                              id=graphene.Int(),
                              name=graphene.String())
    menu = graphene.Field(MenuType,
                          id=graphene.Int()
                          )
    all_restaurant = graphene.List(RestaurantType)
    all_menuCategory = graphene.List(MenuCategoryType)
    all_menu = graphene.List(MenuType)
    all_area = graphene.List(AreaType)

    def resolve_all_area(self, context, **kwargs):
        return Area.objects.all()

    def resolve_all_restaurantCategory(self, context, **kwargs):
        return RestaurantCategory.objects.all()

    def resolve_all_restaurant(self, context, **kwargs):
        return Restaurant.objects.all()

    def resolve_all_menuCategory(self, context, **kwargs):
        return MenuCategory.objects.all()

    def resolve_all_menu(self, context, **kwargs):
        return Menu.objects.all()

    def resolve_restaurant(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Restaurant.objects.get(pk=id)

        if name is not None:
            return Restaurant.objects.get(name=name)
        return None