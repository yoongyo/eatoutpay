import graphene
from graphene_django.types import DjangoObjectType
from .models import PayMethod, Basket
from django.contrib.auth.models import User
import sys
sys.path.append('..')
from restaurant.models import Review, Restaurant


class BasketType(DjangoObjectType):
    class Meta:
        model = Basket


class PayMethodType(DjangoObjectType):
    class Meta:
        model = PayMethod


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
        _basket = Basket.objects.create(user=User.objects.get(id=user), restaurant=Restaurant.objects.get(id=restaurant), sumPrice=sumPrice,
                                        menus=menus, payment=PayMethod.objects.get(id=payment), date=date, dateTime=dateTime)
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
