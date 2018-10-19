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
                generic_description="AI_descr"
                )
        self.BI = AbstractItem.objects.create(
                name="BI_name",
                generic_description="BI_descr"
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
        ai = AbstractItem.objects.get(name="AI_name")
        i_listings = ai.listings.all().values_list('id', flat=True).order_by('id')
        listing_ids = [self.L1.id, self.L2.id, self.L3.id]
        self.assertEqual(list(i_listings), listing_ids)
    def tearDown(self):
        self.Seller.delete()
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

class GetAlternateListings(TestCase):
    # Getting a set of listings from the abstract item of a listing
    def setUp(self):
        self.Seller = User.objects.create(
                username="U_name",
                email="test@example.com",
                first_name="FName",
                last_name="LName"
                )
        self.AI = AbstractItem.objects.create(
                name="AI_name",
                generic_description="AI_descr"
                )
        self.BI = AbstractItem.objects.create(
                name="BI_name",
                generic_description="BI_descr"
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
        self.L5 = Listing.objects.create(
                name="L5_name",
                price=5.00,
                status=True,
                description="L5_descr",
                seller=self.Seller
            )

    def test_get_listing_from_abstract(self):
        listing = Listing.objects.get(name="L1_name")
        i_listings = listing.get_listings().values_list('id', flat=True).order_by('id')
        listing_ids = [self.L1.id, self.L2.id, self.L3.id]
        self.assertEqual(list(i_listings), listing_ids)
        listing = Listing.objects.get(name="L5_name")
        i_listings = listing.get_listings()
        listing_ids = [self.L1.id, self.L2.id, self.L3.id]
        self.assertEqual(i_listings, None)
    def tearDown(self):
        self.Seller.delete()
        self.AI.delete()
        self.BI.delete()
        self.L1.delete()
        self.L2.delete()
        self.L3.delete()
        self.L4.delete()
