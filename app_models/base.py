from django.db import models

# Base model to inherit from


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    deleted = models.BooleanField()

    class Meta:
        abstract = True  # Set this model to be abstract
