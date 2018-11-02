from django.test import TestCase
from .models import User
from .models import Authenticator
from ..listings.models import Listing
from django.utils import timezone

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
        self.user2 = User.objects.create(
            username="user2",
            first_name="fn",
            last_name="ln",
            email="b@b.b"
        )
        self.l1 = Listing.objects.create(
            name="listing a",
            price=1.00,
            seller=self.user1
        )
        self.l2 = Listing.objects.create(
            name="listing b",
            price=2.00,
            seller=self.user1
        )
        self.l3 = Listing.objects.create(
            name="listing c",
            price=3.00,
            seller=self.user2
        )
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

class AuthenticatorTests(TestCase):
    # Testing authenticator
    def setUp(self):
        self.user1 = User.objects.create(
            username="user1",
            first_name="fn",
            last_name="ln",
            email="a@a.a"
        )
        self.user2 = User.objects.create(
            username="user2",
            first_name="fn",
            last_name="ln",
            email="b@b.b"
        )
        self.user3 = User.objects.create(
            username="user3",
            first_name="fn",
            last_name="ln",
            email="c@c.c"
        )
        self.auth1 = Authenticator.objects.create(
            user = self.user1
        )
        self.auth2 = Authenticator.objects.create(
            user = self.user2
        )
    def testAuthenticators(self):
        auth1 = Authenticator.objects.filter(
            user__id = self.user1.id,
            authenticator = self.auth1.authenticator
        )
        self.assertEquals(auth1.exists(), True)
        self.assertEquals(auth1.get().is_expired(), False)
        auth2 = Authenticator.objects.filter(
            user__id = self.user2.id,
            authenticator = self.auth2.authenticator
        )
        self.assertEquals(auth2.exists(), True)
        _auth2 = auth2.get()
        _auth2.datetime_created += timezone.timedelta(days=-7)
        _auth2.save()
        self.assertEquals(auth2.get().is_expired(), True)
        auth3 = Authenticator.objects.filter(
            user__id = self.user3.id,
            authenticator = 2
        )
        self.assertEquals(auth3.exists(), False)
    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()
        self.auth1.delete()
        self.auth2.delete()
