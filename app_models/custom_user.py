from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    bio = models.TextField()
    company = models.CharField(max_length=30)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.username
