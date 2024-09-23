from django.contrib import admin
from .models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(CountryCode)
class CountryCodeAdmin(admin.ModelAdmin):
    pass
