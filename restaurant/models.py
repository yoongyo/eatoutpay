from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse


class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RestaurantCategory(models.Model):
    sequence = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restaurant_category', null=True, blank=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    account = models.CharField(max_length=50)
    tel = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField()
    closedDay = models.CharField(max_length=50)
    representative_menu = models.CharField(max_length=30)
    representative_image = models.ImageField(upload_to='representative_image/', blank=True, null=True)
    businessHours = models.CharField(max_length=50)
    businessLicenseRepresentative = models.CharField(max_length=50)
    businessLicenseMutualName = models.CharField(max_length=50)
    businessLicenseNumber = models.CharField(max_length=50)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follow', blank=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    map_image = models.ImageField(upload_to='map_image/', blank=True, null=True)
    map_content = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def total_likes(self):
        return self.likes.count()  # likes 컬럼의 값의 갯수를 센다

    def get_absolute_url(self):
        return reverse('restaurant:restaurant_detail', args=[self.pk])


class MenuCategory(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    soldOut = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    content = models.TextField()
    image1 = models.ImageField(upload_to='review_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='review_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='review_image/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.restaurant.name





