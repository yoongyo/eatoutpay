import graphene
from graphene_django.types import DjangoObjectType
from .models import PayMethod, Basket


class BasketType(DjangoObjectType):
    class Meta:
        model = Basket


class PayMethodType(DjangoObjectType):
    class Meta:
        model = PayMethod


class CreateBasket(graphene.Mutation):
    user = graphene.Int()
    restaurant = graphene.Int()
    sumPrice = graphene.String()
    menus = graphene.String()
    payment = graphene.Int()
    dataTime = graphene.DateTime()
    date = graphene.Date()

    basket = graphene.Field(BasketType)

    class Arguments:
        user = graphene.ID()
        restaurant = graphene.Int()
        sumPrice = graphene.String()
        menus = graphene.String()
        payment = graphene.Int()
        dateTime = graphene.DateTime()
        date = graphene.Date()

    def mutate(self, info, user, restaurant, sumPrice, menus, payment, dateTime, date):
        _basket = Basket.objects.create(user=user, restaurant=restaurant, sumPrice=sumPrice,
                                       menus=menus, payment=payment, dateTime=date, date=date)
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
