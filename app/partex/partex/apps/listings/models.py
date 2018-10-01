from django.db import models
from ..apps.users import User
from ..apps.reviews import review

# Create your models here.

class Listing(models.Model)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
