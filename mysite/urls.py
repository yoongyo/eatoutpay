from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
