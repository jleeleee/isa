import os
import hmac
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser):
    # Back Accessors:
    #   reviews
    #   authored_reviews
    #   listings
    #   authenticator

    username = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=100, unique=True)

    EXPOSED_FIELDS = ["id", "username", "first_name", "last_name", "date_created"]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_created = models.DateField(auto_now_add=True)

    @property
    def full_name(self):
        return "{} {}".format(first_name, last_name)

    USERNAME_FIELD = 'username'

    def average_reviews(self):
        return self.reviews.all().aggregate(models.Avg('rating'))

    def __str__(self):
        return self.username

    def get_dict(self):
        return { d: getattr(self, d) for d in User.EXPOSED_FIELDS }

class Authenticator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authenticator")
    authenticator = models.CharField(max_length=64) # not primary key because not guaranteed unique

    datetime_created = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        if timezone.now() - self.date_created > timezone.timedelta(days=+7):
            return False
        return True

    def __str__(self):
        return "For {} {}".format(self.user.first_name, self.user.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.authenticator = hmac.new(
                key = settings.SECRET_KEY.encode('utf-8'),
                msg = os.urandom(32),
                digestmod = 'sha256',
            ).hexdigest()
        super(Authenticator, self).save(*args, **kwargs)

    def get_authenticator(self):
        return { "user_id": self.user.id, "auth": self.authenticator }
