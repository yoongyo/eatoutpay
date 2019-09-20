import graphene
from graphene_django.types import DjangoObjectType
from .models import PayMethod, Basket
from restaurant.schema import RestaurantInput
from accounts.schema import UserInput


class BasketType(DjangoObjectType):
    class Meta:
        model = Basket


class PayMethodType(DjangoObjectType):
    class Meta:
        model = PayMethod


class PayMethodInput(graphene.InputObjectType):
    name = graphene.String()
    number = graphene.Int()


class CreateBasket(graphene.Mutation):

    class Arguments:
        user = graphene.Int()
        restaurant = graphene.Int()
        payment = graphene.Int()
        sumPrice = graphene.String()
        menus = graphene.String()
        dateTime = graphene.DateTime()
        date = graphene.Date()

    basket = graphene.Field(BasketType)

    def mutate(self, info, user, restaurant, sumPrice, menus, payment, dateTime, date):
        _basket = Basket.objects.create(user__pk=user, restaurant__pk=restaurant, sumPrice=sumPrice,
                                        menus=menus, payment__pk=payment, date=date, dateTime=dateTime)
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
