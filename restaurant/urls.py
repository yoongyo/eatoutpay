from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    re_path(r'^newRestaurant/$', views.restaurant_new, name='restaurant_new'),
    re_path(r'^$', views.restaurant_list, name='restaurant_list'),
    re_path(r'^(?P<rpk>\d+)/$', views.restaurant_detail, name='restaurant_detail'),
    re_path(r'^(?P<rpk>\d+)/edit/$', views.restaurant_edit, name='restaurant_edit'),
    re_path(r'^(?P<rpk>\d+)/newMenu/$', views.menu_new, name='menu_new'),
    re_path(r'^(?P<rpk>\d+)/menus/$', views.menu_list, name='menu_list'),
    re_path(r'^(?P<rpk>\d+)/(?P<mpk>\d+)/', views.menu_detail, name='menu_detail'),
]


