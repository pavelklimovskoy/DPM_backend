from django.contrib import admin

from .models import AboutPageModel


@admin.register(AboutPageModel)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Отображение модели about в админ панели
    """
    pass
    # def save_model(self, request, obj, form, change):
    #     pass
