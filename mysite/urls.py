from django.conf.urls import re_path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    re_path(r'^', include(('restaurant.urls', 'restaurant'), namespace='restaurant')),
    re_path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
