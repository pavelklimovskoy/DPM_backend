from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Отображение Профилей в админ панели
    """

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="50" ')

    get_image.short_description = "Аватарка сотрудника"
