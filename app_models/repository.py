from django.db import models

from .base import BaseModel
from .user import User


class Repository(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField()
    isPrivate = models.BooleanField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner_user')
    collabarators = models.ManyToManyField(
        User, related_name='collabarator_user')
    forkers = models.ManyToManyField(
        User, related_name='fork_user')
    star_givers = models.ManyToManyField(
        User, related_name='star_user')
