from rest_framework import serializers
from contact_application.serializers import ContactInfoSerializer
from personal_info_application.serializers import PersonalInfoSerializer
from skill_application.serializers import SkillInfoSerializer
from document_application.serializers import DocumentInfoSerializer
from .models import *


class FileInfoSerializer(serializers.ModelSerializer):
    cloud_url = serializers.URLField()
    uploaded_at = serializers.DateTimeField()
    resume_file_name = serializers.CharField()
    parsing_date = serializers.DateTimeField()

    class Meta:
        model = FileInfo
        fields = ('id', 'cloud_url', 'uploaded_at', 'resume_file_name', 'parsing_date')


class CVCategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    sub_category = serializers.CharField()

    class Meta:
        model = CVCategory
        fields = ('id', 'category', 'sub_category')


class CVModelSerializer(serializers.ModelSerializer):
    file_info = FileInfoSerializer()

    document_info = DocumentInfoSerializer()

    cv_category = CVCategorySerializer()
    contact_info = ContactInfoSerializer()

    personal_info = PersonalInfoSerializer()

    skill_info = SkillInfoSerializer()

    class Meta:
        model = CVModel
        fields = '__all__'
