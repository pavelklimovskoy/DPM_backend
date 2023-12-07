from rest_framework import serializers
from .models import *


class PassportDetailSerializer(serializers.ModelSerializer):
    passport_number = serializers.CharField()
    date_of_expire = serializers.CharField()
    date_of_issue = serializers.CharField()
    place_of_issue = serializers.CharField()

    class Meta:
        model = PassportDetailModel
        fields = '__all__'


class DocumentInfoSerializer(serializers.ModelSerializer):
    unique_id = serializers.CharField()
    license_no = serializers.CharField()
    pan_no = serializers.CharField()
    visa_status = serializers.CharField()

    passport_detail = PassportDetailSerializer()

    class Meta:
        model = DocumentInfoModel
        fields = '__all__'
