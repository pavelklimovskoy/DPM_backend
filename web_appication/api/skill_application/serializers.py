from rest_framework import serializers
from .models import *


class SegregatedSkillSerializer(serializers.ModelSerializer):
    skill_type = serializers.CharField()
    skill = serializers.CharField()
    ontology = serializers.CharField()
    alias = serializers.CharField()
    formatted_name = serializers.CharField()
    evidence = serializers.CharField()
    last_used = serializers.CharField()
    experience_in_months = serializers.CharField()

    class Meta:
        model = SegregatedSkillModel
        fields = '__all__'


class SkillInfoSerializer(serializers.ModelSerializer):
    skill_block = serializers.CharField()
    skill_keywords = serializers.CharField()

    segregated_skill = SegregatedSkillSerializer(read_only=True, many=True)

    class Meta:
        model = SkillInfoModel
        fields = '__all__'
