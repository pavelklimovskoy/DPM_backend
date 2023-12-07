from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(FileInfo)
class FileInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(CVCategory)
class CVCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CVModel)
class CVModelAdmin(admin.ModelAdmin):
    pass