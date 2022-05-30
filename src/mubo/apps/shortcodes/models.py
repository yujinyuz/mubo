import random

from django.db import models
from django.db.models.expressions import F
from django.utils.crypto import get_random_string


def generate_short_code() -> str:
    shortcode_length = ShortCode.code.field.max_length  # type: ignore
    return get_random_string(length=random.randint(4, shortcode_length - 2))


class ShortCode(models.Model):

    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    url = models.URLField(help_text="The URL to be shortened")
    code = models.CharField(max_length=8, default=generate_short_code, unique=True)
    hits = models.PositiveBigIntegerField(
        default=0,
        editable=False,
        help_text="Number of times this short code has been hit",
    )

    expires_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.code} - {self.hits}"

    def increment_hits(self):
        self.hits = F("hits") + 1
        self.save(update_fields=["hits"])
        return self
