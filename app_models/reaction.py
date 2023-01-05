from django.db import models
from enumfields import EnumField

from .base import BaseModel
from .enums import ReactionType
from .custom_user import User
from .comment import Comment


class Reaction(BaseModel):
    reaction = EnumField(ReactionType)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
