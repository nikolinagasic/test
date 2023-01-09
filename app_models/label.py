from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .base import BaseModel


class Label(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField()
    # Presuming color will be stored as hex value
    color = models.CharField(max_length=6)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # Make a generic foreign key to make label usable in multiple Models (Issue, PullReqest, etc)
    content_object = GenericForeignKey('content_type', 'object_id')
