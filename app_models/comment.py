from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .base import BaseModel
from .user import User


class Comment(BaseModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # Make a generic foreign key to make comment usable in multiple Models (Issue, PullReqest, etc)
    content_object = GenericForeignKey('content_type', 'object_id')
