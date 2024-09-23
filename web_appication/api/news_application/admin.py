from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(NewsPost)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_image", "date_creation", "is_published", "views_count",)
    list_display_links = ("id", "title",)

    list_filter = ("is_published",)

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.title_image.url} width="50" height="60" ')
