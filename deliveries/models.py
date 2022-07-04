from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    reviewsNum = models.IntegerField(null=True, blank=True, default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



