from django.test import TestCase
from .models import User
from ..listings.models import Listing

# Create your tests here.

class GetUsersListings(TestCase):
    # Getting a set of listings from a certain user
    def setUp(self):
        self.user1 = User.objects.create(
            username="user1",
            first_name="fn",
            last_name="ln",
            email="a@a.a"
        )
        self.user1.save()
        self.user2 = User.objects.create(
            username="user2",
            first_name="fn",
            last_name="ln",
            email="b@b.b"
        )
        self.user2.save()
        self.l1 = Listing.objects.create(
            name="listing a",
            price=1.00,
            seller=self.user1
        )
        self.l1.save()
        self.l2 = Listing.objects.create(
            name="listing b",
            price=2.00,
            seller=self.user1
        )
        self.l2.save()
        self.l3 = Listing.objects.create(
            name="listing c",
            price=3.00,
            seller=self.user2
        )
        self.l3.save()
    def testGetListings(self):
        u1 = User.objects.get(username="user1")
        l1 = Listing.objects.get(name="listing a")
        l2 = Listing.objects.get(name="listing b")
        listing_ids = [l1.id, l2.id]
        u_listings = u1.listings.all().values_list('id', flat=True).order_by('id')
        self.assertEqual(list(u_listings), listing_ids)
        u2 = User.objects.get(username="user2")
        l3 = Listing.objects.get(name="listing c")
        u_listings = u2.listings.all().values_list('id', flat=True).order_by('id')
        self.assertEquals(list(u_listings), [l3.id])
    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.l1.delete()
        self.l2.delete()
        self.l3.delete()
