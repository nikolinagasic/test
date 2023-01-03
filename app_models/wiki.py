from django.db import models

from .base import BaseModel
from .repository import Repository


class Wiki(BaseModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
