from rest_framework import serializers
from cv_application.serializers import CVModelSerializer

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.URLField()
    langauge = serializers.CharField()

    uploaded_cv = CVModelSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
