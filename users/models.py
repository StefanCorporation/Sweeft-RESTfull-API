from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


