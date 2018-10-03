from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    # Back Accessors:
    #   reviews
    #   authored_reviews
    #   listings
    username = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=100, unique=True)

    EXPOSED_FIELDS = ["username", "first_name", "last_name", "date_created"]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_created = models.DateField(auto_now_add=True)

    @property
    def full_name(self):
        return "{} {}".format(first_name, last_name)

    USERNAME_FIELD = 'username'

    def average_reviews(self):
        return reviews.all().aggregate(Avg('rating'))

    def __str__(self):
        return self.username

    def get_dict(self):
        return { d: getattr(self, d) for d in User.EXPOSED_FIELDS }
