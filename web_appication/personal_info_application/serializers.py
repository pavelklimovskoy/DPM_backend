from rest_framework import serializers
from contact_application.serializers import ContactInfoSerializer
from .models import *

from country_application.serializers import CountrySerializer


class LanguageSerializer(serializers.Serializer):
    language = serializers.CharField()
    language_code = serializers.CharField()

    class Meta:
        model = NameModel
        fields = ['__all__']


class NameSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    titled_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    formatted_name = serializers.CharField()

    confidence_score = serializers.IntegerField()

    class Meta:
        model = LanguageModel
        fields = ['__all__']


class PersonalInfoSerializer(serializers.Serializer):
    name = NameSerializer()

    date_of_birth = serializers.DateTimeField()
    gender = serializers.CharField()

    father_name = serializers.CharField()
    mother_name = serializers.CharField()

    language_known = LanguageSerializer()

    hobbies = serializers.CharField()
    martial_status = serializers.CharField()
    nationality = serializers.CharField()

    objectives = serializers.CharField()
    achievements = serializers.CharField()

    resume_language = LanguageSerializer()
    resume_country = CountrySerializer()

    class Meta:
        model = PersonalInfoModel
        fields = ['__all__']

