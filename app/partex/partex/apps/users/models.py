from django.db import models
from django.contrib.auth.models import AbstractUser
from ..apps.reviews import UserReview

# Create your models here.

class User(AbstractUser):
    reviews = models.ManyToManyField(UserReview)

    def average_reviews():
        reviews.all().aggregate(Avg('rating'))
