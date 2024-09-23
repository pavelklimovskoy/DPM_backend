from django.contrib import admin
from .models import *


@admin.register(PassportDetailModel)
class PassportDetailAdmin(admin.ModelAdmin):
    """
    Отображение паспортных данных в админ панели
    """
    pass


@admin.register(DocumentInfoModel)
class DocumentInfoAdmin(admin.ModelAdmin):
    """
    Отображение информации о документах в админ панели
    """
    pass
