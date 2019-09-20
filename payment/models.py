from django.db import models
import sys
sys.path.append('..')
from restaurant.models import Review, Restaurant
from django.conf import settings


class PayMethod(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    sumPrice = models.CharField(max_length=50)
    menus = models.CharField(max_length=200)
    payment = models.ForeignKey(PayMethod, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
