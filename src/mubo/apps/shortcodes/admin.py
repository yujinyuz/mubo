from django.contrib import admin

from .models import ShortCode


@admin.register(ShortCode)
class ShortCodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "url",
        "code",
        "hits",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "created_at", "updated_at")
    date_hierarchy = "created_at"
