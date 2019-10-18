from django.contrib import admin
from .models import Restaurant, RestaurantCategory, MenuCategory, Area, Menu, Review, Region
from django import forms
from ckeditor.widgets import CKEditorWidget


class RestaurantCategoryAdmin(admin.ModelAdmin):
    # description = forms.CharField(widget=CKEditorWidget())
    list_display = ['name']

    class Meta:
        model = Restaurant


class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']


class MethodAdmin(admin.ModelAdmin):
    list_display = ['name']


class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['restaurant']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'pk']


admin.site.register(Region, RegionAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(RestaurantCategory, RestaurantCategoryAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review, ReviewAdmin)


