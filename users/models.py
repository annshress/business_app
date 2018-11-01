import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

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

    class Meta:
        swappable = "AUTH_USER_MODEL"
