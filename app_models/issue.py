from django.db import models
from enumfields import EnumField

from .base import BaseModel
from .enums import IssueStatus
from .repository import Repository
from .custom_user import User


class Issue(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField()
    state = EnumField(IssueStatus, default=IssueStatus.OPENED)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
