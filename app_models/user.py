from django.db import models

from .base import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    bio = models.TextField()
    company = models.CharField(max_length=30)
    website = models.CharField(max_length=100)
