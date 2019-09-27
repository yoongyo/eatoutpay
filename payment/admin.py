from django.contrib import admin
from .models import Basket, PayMethod


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'restaurant', 'payment', 'sumPrice', 'menus']


class PayMethodAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Basket, BasketAdmin)
admin.site.register(PayMethod, PayMethodAdmin)

