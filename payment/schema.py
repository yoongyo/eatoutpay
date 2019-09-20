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

    class Arguments:
        user = graphene.Int()
        restaurant = graphene.Int()
        sumPrice = graphene.String()
        menus = graphene.String()
        payment = graphene.Int()
        dateTime = graphene.DateTime()
        date = graphene.Date()

    def mutate(self, user, restaurant, sumPrice, menus, payment, dateTime, date):
        basket = Basket(user=user, restaurant=restaurant, sumPrice=sumPrice, menus=menus,
                        payment=payment, date=date, dateTime=dateTime)
        basket.save()

        return CreateBasket(
            user=basket.user,
            restaurant=basket.restaurant,
            sumPrice=basket.sumPrice,
            menus=basket.menus,
            payment=payment,
            dateTime=dateTime,
            date=date
        )


class Query(graphene.AbstractType):
    all_payMethod = graphene.List(PayMethodType)

    all_basket = graphene.List(BasketType)

    def resolve_all_payMethod(self, context, **kwargs):
        return PayMethod.objects.all()

    def resolve_all_basket(self, context, **kwargs):
        return Basket.objects.all()


class Mutation(graphene.ObjectType):
    create_basket = CreateBasket.Field()
