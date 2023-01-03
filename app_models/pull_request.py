from django.db import models
from enumfields import EnumField

from .base import BaseModel
from .user import User
from .branch import Branch
from .enums import PullRequestStatus


class PullRequest(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField()
    state = EnumField(PullRequestStatus, default=PullRequestStatus.OPENED)
    base = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name='base_branch')
    compare = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name='compare_branch')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
