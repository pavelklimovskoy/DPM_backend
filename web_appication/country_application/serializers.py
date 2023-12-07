from rest_framework import serializers
from contact_application.serializers import ContactInfoSerializer
from .models import *


class CountryCodeSerializer(serializers.ModelSerializer):
    iso_alpha2 = serializers.CharField()
    iso_alpha3 = serializers.CharField()
    UN_code = serializers.CharField()

    class Meta:
        model = CountryCode
        fields = ('id', 'iso_alpha2', 'iso_alpha3', 'UN_code')


class CountrySerializer(serializers.ModelSerializer):
    country = serializers.CharField()
    evidence = serializers.CharField()
    country_code = CountryCodeSerializer()

    class Meta:
        model = Country
        fields = ('id', 'country', 'evidence', 'country_code')
