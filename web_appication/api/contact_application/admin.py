from django.contrib import admin
from .models import *


@admin.register(EmailContact)
class EmailContactAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneNumberContact)
class PhoneNumberContactAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailInfo)
class EmailInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass
