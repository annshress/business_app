from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from books.utils import CATEGORY

PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{7,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")


class Publisher(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    contact = models.CharField(_("Contact"), max_length=512)
    phone = models.CharField(
        _("Phone"),
        max_length=16,
        validators=[PHONE_REGEX]
    )

    def __str__(self):
        return f'{self.name}, {self.contact}'


class BookManager(models.Manager):
    def books_bought_average_price(self, user):
        return self.get_queryset().filter(bought_by=user).aggregate(avg_price=Avg('price'))['avg_price']

    def books_bought_minimum_price(self, user):
        return self.get_queryset().filter(bought_by=user).aggregate(min_price=Min('price'))['min_price']

    def books_bought_maximum_price(self, user):
        return self.get_queryset().filter(bought_by=user).aggregate(max_price=Max('price'))['max_price']

    def books_bought_count(self, user, category=None):
        q = self.get_queryset().filter(bought_by=user)
        if category:
            return q.filter(category=category)
        return q.count()


class Book(models.Model):
    CATEGORY_CHOICES = (
        (CATEGORY.adventure, _("adventure")),
        (CATEGORY.horror, _("horror")),
        (CATEGORY.fiction, _("fiction")),
        (CATEGORY.science, _("science")),
        (CATEGORY.biography, _("biography"))
    )

    isbn = models.CharField(_("ISBN"), max_length=64)
    name = models.CharField(_("Name"), max_length=512)
    pages = models.PositiveIntegerField(
        _("Page Count"),
        validators=[
            MinValueValidator(1, "Should have at least a page")
        ]
    )
    price = models.FloatField(
        _("Price"),
        validators=[
            MinValueValidator(1, "Price can't be less than 1")
        ]
    )
    category = models.PositiveSmallIntegerField(
        _("Category"),
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False
    )
    publisher = models.ForeignKey(
        "books.Publisher",
        on_delete=models.CASCADE,
        related_name="books"
    )
    bought_by = models.ManyToManyField("users.AayuUser",
                                       related_name="books_bought")

    @classmethod
    def get_category(cls, ind):
        return list(filter(lambda x: x[0] == ind, cls.CATEGORY_CHOICES))[0][1]

    objects = BookManager()

    def get_absolute_url(self):
        return reverse("books:detail", kwargs=dict(pk=self.pk))

    def get_list_absolute_url(self):
        return reverse("books:list")

    def __str__(self):
        return f"{self.name} {self.publisher.name}"
