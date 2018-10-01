from django.db import models

from ..apps.users.models import User
from ..apps.listings.models import Listing

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=300)
    rating = models.IntegerField(min_value=0,max_value=5)
    body = models.TextField()
    author = models.ForeignKey(User)

class UserReview(Review):
    subject = models.ForeignKey(User)

class ListingReview(Review):
    subject = models.ForeignKey(Listing)
