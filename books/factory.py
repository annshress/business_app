import factory

from books.models import Publisher, Book
from books.utils import CATEGORY
from users.models import AayuUser


class PublisherFactory(factory.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = factory.Sequence(lambda n: "EktaPub%d" % n)
    contact = factory.Sequence(lambda n: "Area%d, City%d" % (n, n))
    phone = factory.Sequence(lambda n: "9988900%d" % n)


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book

    isbn = factory.Sequence(lambda n: "this_a_Isbn%d" % n)
    name = factory.Sequence(lambda n: "NameBook%d" % n)
    pages = factory.Iterator([200, 300, 500, 900])
    price = factory.Iterator([190, 300, 550, 750])
    category = factory.Iterator(
        [CATEGORY.adventure, CATEGORY.horror, CATEGORY.fiction]
    )
    publisher = factory.SubFactory(PublisherFactory)


class AayuUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = AayuUser

    username = factory.Sequence(lambda n: "username%d" % n)
    first_name = factory.Sequence(lambda n: "First%d" % n)
    last_name = factory.Sequence(lambda n: "Last%d" % n)
    email = factory.Sequence(lambda n: "django%d@wokay.com" % n)
