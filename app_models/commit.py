from django.db import models

from .base import BaseModel
from .user import User
from .branch import Branch


class Commit(BaseModel):
    message = models.CharField(max_length=100)
    description = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    commited_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
