from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from books.utils import CATEGORY


class Publisher(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    date_of_birth = models.DateTimeField(_("DOB"), blank=False)


class Book(models.Model):
    CATEGORY_CHOICES = (
        (CATEGORY.adventure, _("adventure")),
        (CATEGORY.horror, _("horror")),
        (CATEGORY.fiction, _("fiction")),
        (CATEGORY.science, _("science")),
        (CATEGORY.biography, _("biography"))
    )

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
    bought_by = models.ManyToManyField("users.AayuUser", related_name="books_bought")
