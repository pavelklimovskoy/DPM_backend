from django.db import models
from country_application.models import CountryCode


class LocationModel(models.Model):
    city = models.CharField()
    state = models.CharField()
    state_iso_code = models.CharField()
    country = models.CharField()
    country_code = models.ManyToManyField(CountryCode)
