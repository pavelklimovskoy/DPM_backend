from django.db import models


class CountryCode(models.Model):
    iso_alpha2 = models.CharField(
        default="-1",
        max_length=254
    )
    iso_alpha3 = models.CharField(
        default="-1",
        max_length=254
    )
    UN_code = models.CharField(
        default="-1",
        max_length=254
    )


class Country(models.Model):
    country = models.CharField(
        default='unknown',
        max_length=256
    )
    evidence = models.CharField(
        default='unknown',
        max_length=256
    )

    country_code = models.OneToOneField(CountryCode, on_delete=models.DO_NOTHING, null=True)
