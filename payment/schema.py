import graphene
from graphene_django.types import DjangoObjectType
from .models import PayMethod, Basket
from restaurant.schema import RestaurantType
from accounts.schema import UserType

class BasketType(DjangoObjectType):
    class Meta:
        model = Basket


class PayMethodType(DjangoObjectType):
    class Meta:
        model = PayMethod


class BasketInput(graphene.InputObjectType):
    user = graphene.Field(UserType)
    restaurant = graphene.Field(RestaurantType)
    sumPrice = graphene.String()
    menus = graphene.String()
    payment = graphene.Field(PayMethodType)
    dataTime = graphene.DateTime()
    date = graphene.Date()


class CreateBasket(graphene.Mutation):
    basket = graphene.Field(BasketType)

    class Arguments:
        basket_data = BasketInput(required=True)

    def mutate(self, info, basket_data):
        _basket = Basket.objects.create(**basket_data)
        return CreateBasket(basket=_basket)


class Query(graphene.AbstractType):
    all_payMethod = graphene.List(PayMethodType)

    all_basket = graphene.List(BasketType)

    def resolve_all_payMethod(self, context, **kwargs):
        return PayMethod.objects.all()

    def resolve_all_basket(self, context, **kwargs):
        return Basket.objects.all()


class Mutation(graphene.ObjectType):
    create_basket = CreateBasket.Field()
