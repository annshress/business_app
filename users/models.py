import os

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models.aggregates import Avg, Min, Max, Count

from books.models import Book

IMG_PATH = os.path.join('aayu', 'users')


def get_image_path(f, instance):
    """
    :param instance: AayuUser
    """
    os.remove(instance.image.full_path)
    return os.path.join(IMG_PATH, f.filename)


class AayuUser(AbstractUser):
    image = models.ImageField(
        _("Image"),
        upload_to=get_image_path,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs=dict(pk=self.pk))

    def get_list_absolute_url(self):
        return reverse("users:list")

    def get_books_bought(self, category=None):
        q = self.books_bought.all()
        if category is not None:
            q = q.filter(category=category)
        if not q.exists():
            raise ValueError
        return q

    def books_bought_average_price(self, category=None):
        try:
            return "%.2f" % self.get_books_bought(category=category).aggregate(avg_price=Avg('price'))['avg_price']
        except ValueError:
            return 0

    def books_bought_minimum_price(self, category=None):
        try:
            return "%.2f" % self.get_books_bought(category=category).aggregate(min_price=Min('price'))['min_price']
        except ValueError:
            return 0

    def books_bought_maximum_price(self, category=None):
        try:
            return "%.2f" % self.get_books_bought(category=category).aggregate(max_price=Max('price'))['max_price']
        except ValueError:
            return 0

    def costliest_bought_book(self, category=None):
        try:
            return self.get_books_bought(category=category).order_by('price').last()
        except ValueError:
            return

    def cheapest_bought_book(self, category=None):
        try:
            return self.get_books_bought(category=category).order_by('-price').last()
        except ValueError:
            return

    def books_bought_count(self, category=None):
        try:
            return self.get_books_bought(category=category).count()
        except ValueError:
            return 0

    def loved_category(self):
        try:
            loved = self.get_books_bought().\
                values('category').annotate(cat_count=Count('category')).\
                values('category', 'cat_count').order_by('-cat_count')[0]['category']
            loved = Book.get_category(loved)
        except ValueError:
            return
        return loved

    class Meta:
        swappable = "AUTH_USER_MODEL"
