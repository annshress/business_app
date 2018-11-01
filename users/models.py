from django.contrib.auth.models import AbstractUser


class AayuUser(AbstractUser):
    class Meta:
        swappable = "AUTH_USER_MODEL"
