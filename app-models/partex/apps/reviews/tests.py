from django.test import TestCase
from .models import UserReview, ItemReview
from ..users.models import User
from ..listings.models import AbstractItem

class GetReviews(TestCase):
    # Getting a set of listings from a certain user
    def setUp(self):
        self.user1 = User.objects.create(
            username="reviewer1",
            first_name="fn1",
            last_name="ln1",
            email="a@a.a"
        )

        self.user2 = User.objects.create(
            username="reviewer2",
            first_name="fn2",
            last_name="ln2",
            email="b@b.b"
        )
        self.seller = User.objects.create(
            username="seller",
            first_name="fn",
            last_name="ln",
            email="c@c.c"
        )
        self.review_u1 = UserReview.objects.create(
            title="UserReview 1",
            rating=2,
            body="UserReview test 1",
            author=self.user1,
            subject=self.seller
        )
        self.review_u2 = UserReview.objects.create(
            title="UserReview 2",
            rating=4,
            body="UserReview test 2",
            author=self.user2,
            subject=self.seller
        )

        self.item = AbstractItem.objects.create(
            name="item a",
            generic_description="description"
        )
        self.review_i1 = ItemReview.objects.create(
            title="ItemReview 1",
            rating=2,
            body="ItemReview test 1",
            author=self.user1,
            subject=self.item
        )
        self.review_i2 = ItemReview.objects.create(
            title="ItemReview 2",
            rating=4,
            body="ItemReview test 2",
            author=self.user2,
            subject=self.item
        )


    def test_all_user_review(self):
        seller = User.objects.get(username="seller")
        reviewer1 = User.objects.get(username="reviewer1")
        reviewer2 = User.objects.get(username="reviewer2")
        review_u1 = UserReview.objects.get(title="UserReview 1")
        review_u2 = UserReview.objects.get(title="UserReview 2")

        reviews = [review_u1, review_u2]
        review_ids = [r.id for r in reviews]

        u_listings = seller.reviews.all().values_list('id', flat=True).order_by('id')
        self.assertEqual(list(u_listings), review_ids)

    def test_item_review(self):
        item = AbstractItem.objects.get(name="item a")
        reviewer1 = User.objects.get(username="reviewer1")
        reviewer2 = User.objects.get(username="reviewer2")
        review_i1 = ItemReview.objects.get(title="ItemReview 1")
        review_i2 = ItemReview.objects.get(title="ItemReview 2")
        
        reviews = [review_i1, review_i2]
        review_ids = [r.id for r in reviews]

        i_listings = item.reviews.all().values_list('id', flat=True).order_by('id')
        self.assertEqual(list(i_listings), review_ids)

    def test_avg_user_review(self):
        seller = User.objects.get(username="seller")
        avg_review = seller.average_reviews()['rating__avg']
        self.assertEqual(3, avg_review)

    def test_avg_item_review(self):
        item = AbstractItem.objects.get(name="item a")
        avg_review = item.average_reviews()['rating__avg']
        self.assertEqual(3, avg_review)


    def test_review_from_review_user(self):
        review1 = UserReview.objects.get(title="UserReview 1")
        u_reviews = review1.subject.reviews.all().values_list('id', flat=True).order_by('id')
        review_ids = [self.review_u1.id, self.review_u2.id]
        self.assertEqual(list(u_reviews), review_ids)

    def test_review_from_review_item(self):
        review1 = ItemReview.objects.get(title="ItemReview 1")
        u_reviews = review1.subject.reviews.all().values_list('id', flat=True).order_by('id')
        review_ids = [self.review_i1.id, self.review_i2.id]
        self.assertEqual(list(u_reviews), review_ids)

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.seller.delete()
        self.review_u1.delete()
        self.review_u2.delete()
        self.item.delete()
        self.review_i1.delete()
        self.review_i2.delete()

