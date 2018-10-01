from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    reviews = models.ManyToManyField("reviews.UserReview")

    def average_reviews(self):
        reviews.all().aggregate(Avg('rating'))

    def __str__(self):
        return self.username
