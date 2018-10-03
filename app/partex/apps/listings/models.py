from django.db import models
from ..users.models import User

# Create your models here.

class AbstractItem(models.Model):
    # Back Accessors:
    #   reviews
    #   listings
    EXPOSED_FIELDS = ["id", "name", "generic_description"]
    name = models.CharField(max_length=200, unique=True)
    generic_description = models.TextField(blank=True)
    #reference_image = models.ImageField(upload_to='ref_images/{}/'.format(name), blank=True)

    def __str__(self):
        return self.name

    def get_dict(self):
        return { d: getattr(self, d) for d in AbstractItem.EXPOSED_FIELDS }

class Listing(models.Model):
    EXPOSED_FIELDS = ["id", "name", "price", "status", "description", "date_created"]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    base_item = models.ForeignKey(AbstractItem, blank=True, on_delete=models.CASCADE, related_name="listings")

    date_created = models.DateField(auto_now_add=True)

    def average_reviews(self):
        return reviews.all().aggregate(Avg('rating'))

    def __str__(self):
        return self.name

    def get_dict(self):
        ret_dict = { d: getattr(self, d) for d in Listing.EXPOSED_FIELDS }
        ret_dict["seller"] = self.seller.id
        ret_dict["base_item"] = self.base_item.id
        return ret_dict
