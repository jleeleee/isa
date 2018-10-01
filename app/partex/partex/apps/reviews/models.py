from django.db import models

from ..apps.users.models import User
from ..apps.listings.models import Listing

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=300)
    rating = models.IntegerField()
    body = models.TextField()

class UserReview(Review):
    author = models.ForeignKey(User)
    subject = models.ForeignKey(User)

class ListingReview(Review):
    author = models.ForeignKey(User)
    subject = models.ForeignKey(Listing)
