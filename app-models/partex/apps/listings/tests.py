from django.test import TestCase
from .models import AbstractItem, Listing
from ..users.models import User
# Create your tests here.

class GetListingsFromAbstract(TestCase):
    # Getting a set of listings by looking at an abstract item
    def setUp(self):
        self.Seller = User.objects.create(
                username="U_name",
                email="test@example.com",
                first_name="FName",
                last_name="LName"
                )
        self.AI = AbstractItem.objects.create(
                name="AI_name",
                generic_description="AI_descr",
                )
        self.BI = AbstractItem.objects.create(
                name="BI_name",
                generic_description="BI_descr",
                )
        self.L1 = Listing.objects.create(
                name="L1_name",
                price=1.00,
                status=True,
                description="L1_descr",
                base_item=self.AI,
                seller=self.Seller
            )
        self.L2 = Listing.objects.create(
                name="L2_name",
                price=2.00,
                status=False,
                description="L2_descr",
                base_item=self.AI,
                seller=self.Seller
            )
        self.L3 = Listing.objects.create(
                name="L3_name",
                price=3.00,
                status=True,
                description="L3_descr",
                base_item=self.AI,
                seller=self.Seller
            )
        self.L4 = Listing.objects.create(
                name="L4_name",
                price=4.00,
                status=True,
                description="L4_descr",
                base_item=self.BI,
                seller=self.Seller
            )
    def test_get_listing_from_abstract(self):
        print("testing test")
        self.assertEqual(True, True)

    def tearDown(self):
        self.AI.delete()
        self.BI.delete()
        self.L1.delete()
        self.L2.delete()
        self.L3.delete()
        self.L4.delete()

class getReviewsOfSeller(TestCase):
    # Getting the reviews of the seller of a listing
    def setUp(self):
        pass
    def success_response(self):
        pass
    def fails_invalid(self):
        pass
    def tearDown(self):
        pass

class getReviewsOfAbstract(TestCase):
    # Getting the reviews of an AbstractItem
    def setUp(self):
        pass
    def success_response(self):
        pass
    def fails_invalid(self):
        pass
    def tearDown(self):
        pass

class getAlternateListings(TestCase):
    # Getting listings with same AbstractItems as this AbstractItem
    def setUp(self):
        pass
    def success_response(self):
        pass
    def fails_invalid(self):
        pass
    def tearDown(self):
        pass
