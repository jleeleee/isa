from django.db import models

from ..users.models import User
from ..listings.models import Listing, AbstractItem

# Create your models here.
class Review(models.Model):
    EXPOSED_FIELDS = ["id", "title", "rating", "body", "date_created"]
    title = models.CharField(max_length=300)
    rating = models.IntegerField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authored_reviews")

    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_dict(self):
        ret_dict = { d: getattr(self, d) for d in Review.EXPOSED_FIELDS }

class UserReview(Review):
    subject = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.title
    def get_dict(self):
        ret_dict = { d: getattr(self, d) for d in UserReview.EXPOSED_FIELDS }
        ret_dict["author"] = self.author.id
        ret_dict["subject"] = self.subject.id
        return ret_dict

class ItemReview(Review):
    subject = models.ForeignKey(AbstractItem, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.title
    def get_dict(self):
        ret_dict = { d: getattr(self, d) for d in ItemReview.EXPOSED_FIELDS }
        ret_dict["author"] = self.author.id
        ret_dict["subject"] = self.subject.id
        return ret_dict
