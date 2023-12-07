from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Отображение сотрудников в админ панели
    """

    list_display = ('id', 'fullname_ru', 'position_ru', 'is_showed', 'get_image')
    list_display_links = ("fullname_ru",)
    readonly_fields = ("get_image",)

    list_filter = ("is_showed",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="50" ')

    get_image.short_description = "Аватарка сотрудника"
