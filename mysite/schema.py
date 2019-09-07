import graphene
from restaurant.schema import Query as RestaurantQuery
from accounts.schema import Query as UserQuery


class Querys(RestaurantQuery, UserQuery, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass


schema = graphene.Schema(query=Querys)