from django.db import models

from .base import BaseModel
from .custom_user import User


class Repository(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    isPrivate = models.BooleanField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner_user')
    collabarators = models.ManyToManyField(
        User, related_name='collabarator_user', blank=True)
    forkers = models.ManyToManyField(
        User, related_name='fork_user', blank=True)
    star_givers = models.ManyToManyField(
        User, related_name='star_user', blank=True)
