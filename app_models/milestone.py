from django.db import models
from enumfields import EnumField

from app_models.enums import MilestoneState

from .base import BaseModel
from .project import Project


class Milestone(BaseModel):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateField()
    state = EnumField(MilestoneState)
    milestone = models.ForeignKey(Project, on_delete=models.CASCADE)

