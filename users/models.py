from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        max_length=150,
        verbose_name='email',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



