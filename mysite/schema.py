from restaurant.schema import Query as RestaurantQuery
from accounts.schema import Query as UserQuery
from accounts.schema import Mutation as UserMutation
import graphene
import graphql_jwt


class Query(RestaurantQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)