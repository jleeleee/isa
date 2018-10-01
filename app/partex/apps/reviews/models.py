from django.db import models

from ..users.models import User
from ..listings.models import Listing

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=300)
    rating = models.IntegerField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserReview(Review):
    subject = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ListingReview(Review):
    subject = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
