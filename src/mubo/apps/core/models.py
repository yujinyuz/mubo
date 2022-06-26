import uuid_extensions
from django.db import models


def generate_uuid7():
    return uuid_extensions.uuid7()


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=generate_uuid7,
        editable=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
