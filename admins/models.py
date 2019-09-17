from django.db import models
from django.conf import settings
import sys
sys.path.append('..')
from restaurant.models import Review, Restaurant


class AdminComment(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    targetReview = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)