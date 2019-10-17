from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^getRegion/$', views.getRegion, name='getArea'),
    re_path(r'^getArea/$', views.getArea),
    re_path(r'^api/reviews/$', views.ReviewViewSet.as_view(), name='reviews'),
    re_path(r'^newRestaurant/$', views.restaurant_new, name='restaurant_new'),
    re_path(r'^$', views.restaurant_detail, name='restaurant_detail'),
    re_path(r'^edit/$', views.restaurant_edit, name='restaurant_edit'),
    re_path(r'^newMenu/$', views.menu_new, name='menu_new'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.menu_edit, name='menu_edit'),
    re_path(r'^(?P<pk>\d+)/$', views.menu_detail, name='menu_detail'),
]


