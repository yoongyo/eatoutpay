from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from . models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=False)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType,
                          username=graphene.String()
                          )

    user = graphene.Field(UserType,
                          username=graphene.String()
                          )
    profiles = graphene.List(ProfileType)

    def resolve_user(self, info, **kwargs):
        username = kwargs.get("username")

        if username is not None:
            return get_user_model().objects.get(username=username)

        return None

    def resolve_profiles(self, info):
        return Profile.objects.all()

    def resolve_users(self, info, **kwargs):
        username = kwargs.get("username")

        if username is not None:
            get_user_model().objectsa.filter(username=username)

        return get_user_model().objects.all()