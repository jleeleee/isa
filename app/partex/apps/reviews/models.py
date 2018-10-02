from django.db import models

from ..users.models import User
from ..listings.models import Listing, AbstractItem

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=300)
    rating = models.IntegerField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authored_reviews")

    def __str__(self):
        return self.title

class UserReview(Review):
    subject = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.title

class ItemReview(Review):
    subject = models.ForeignKey(AbstractItem, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.title
