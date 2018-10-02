from django.db import models
from ..users.models import User

# Create your models here.

class AbstractItem(models.Model):
    name = models.CharField(max_length=200)
    reviews = models.ManyToManyField("reviews.ItemReview")

    def __str__(self):
        return self.name

class Listing(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    base_item = models.ForeignKey(AbstractItem, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
