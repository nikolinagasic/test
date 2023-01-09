from django.db import models

from .base import BaseModel
from .repository import Repository


class Branch(BaseModel):
    name = models.CharField(max_length=100)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
