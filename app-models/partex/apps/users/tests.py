from django.test import TestCase
from .models import User
from ..listings.models import Listing

# Create your tests here.

class GetUsersListings(TestCase):
    # Getting a set of listings from a certain user
    def setUp(self):
        user1 = user.objects.create(
            name="user1",
            first_name="fn",
            last_name="ln"
        ).save()
        user2 = user.objects.create(
            name="user2",
            first_name="fn",
            last_name="ln"
        ).save()
        Listing.objects.create(
            name="listing a",
            price=1.00,
            seller=user1
        ).save()
        Listing.objects.create(
            name="listing b",
            price=2.00,
            seller=user1
        ).save()
        Listing.objects.create(
            name="listing c",
            price=3.00,
            seller=user2
        ).save()
    def getListings(self):
        u1 = User.objects.get(name="user1")
        l1 = Listing.objects.get(name="listing a")
        l2 = Listing.objects.get(name="listing b")
        listing_ids = [l1.id, l2.id].sort()
        self.assertEqual(u.listings.value_list('id', flat=True).order_by('id'), listing_ids)
        u2 = User.objects.get(name="user2")
        l3 = Listing.objects.get(name="listing c")
        self.assertEquals(u2.listings.value_list('id', flat=True).order_by('id'), [l3.id])
    def tearDown(self):
        pass
