from django.db import models
from app_models.repository import Repository
from enumfields import EnumField

from .base import BaseModel
from .repository import Repository


class Project(BaseModel):
    title = models.TextField()
    description = models.TextField()
    repository = models.ForeignKey(Repository, on_delete=models.DO_NOTHING)
