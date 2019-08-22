import graphene
from restaurant.schema import Query as RestaurantQuery


class Querys(RestaurantQuery, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass


schema = graphene.Schema(query=Querys)