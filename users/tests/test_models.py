from django.test.testcases import TestCase

from books.factory import AayuUserFactory, BookFactory


class TestUserModel(TestCase):
    def setUp(self):
        self.user = AayuUserFactory.create()
        self.book1 = BookFactory.create(price=100, category=0)
        self.book2 = BookFactory.create(price=200, category=0)
        self.book3 = BookFactory.create(price=300, category=1)
        self.book1.bought_by.add(self.user)
        self.book2.bought_by.add(self.user)
        self.book3.bought_by.add(self.user)

    def test_001_get_absolute_url(self):
        self.fail()

    def test_002_get_books_bought(self):
        self.fail()

    def test_003_books_bought_average_price(self):
        self.fail()

    def test_004_books_bought_minimum_price(self):
        self.fail()

    def test_005_books_bought_maximum_price(self):
        self.fail()

    def test_006_costliest_bought_book(self):
        self.fail()

    def test_007_cheapest_bought_book(self):
        self.fail()

    def test_008_books_bought_count(self):
        self.fail()

    def test_009_loved_category(self):
        self.fail()
