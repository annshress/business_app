from django.test.testcases import TestCase
from django.urls import reverse

from books.factory import AayuUserFactory, BookFactory
from books.models import Book


class TestUserModel(TestCase):
    def setUp(self):
        self.user = AayuUserFactory.create()
        self.cat1 = 0
        self.cat2 = 1
        self.book1 = BookFactory.create(price=100, category=self.cat1)
        self.book2 = BookFactory.create(price=200, category=self.cat1)
        self.book3 = BookFactory.create(price=300, category=self.cat2)
        self.book1.bought_by.add(self.user)
        self.book2.bought_by.add(self.user)
        self.book3.bought_by.add(self.user)

    def test_001_get_absolute_url(self):
        self.assertIsInstance(self.user.get_absolute_url(), str)
        self.assertEqual(self.user.get_absolute_url(),
                         reverse('users:detail', kwargs=dict(pk=self.user.pk)))

    def test_002_get_books_bought(self):
        self.assertCountEqual(self.user.get_books_bought(),
                         Book.objects.all())
        self.assertCountEqual(self.user.get_books_bought(0),
                         Book.objects.filter(category=0))

    def test_003_books_bought_average_price(self):
        self.assertEqual(float(self.user.books_bought_average_price()),
                         200)

    def test_004_books_bought_minimum_price(self):
        self.assertEqual(float(self.user.books_bought_minimum_price()),
                         100)

    def test_005_books_bought_maximum_price(self):
        self.assertEqual(float(self.user.books_bought_maximum_price()),
                         300)

    def test_006_costliest_bought_book(self):
        self.assertEqual(self.user.costliest_bought_book(),
                         self.book3)

    def test_007_cheapest_bought_book(self):
        self.assertEqual(self.user.cheapest_bought_book(),
                         self.book1)

    def test_008_books_bought_count(self):
        self.assertEqual(self.user.books_bought_count(),
                         3)

    def test_009_loved_category(self):
        self.assertEqual(self.user.loved_category(),
                         Book.get_category(self.cat1))
