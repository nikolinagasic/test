from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .base import BaseModel
from .pull_request import PullRequest
from .user import User
from .enums import PullRequestActions


class PullRequestUpdateEvent(BaseModel):
    pull_reqest = models.ForeignKey(PullRequest, on_delete=models.DO_NOTHING)
    action: PullRequestActions
