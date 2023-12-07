from rest_framework import serializers

from .models import *


class EmailContactSerializer(serializers.ModelSerializer):
    email_address = serializers.EmailField()
    confidence_score = serializers.IntegerField()

    class Meta:
        model = EmailContact
        fields = ('id', 'email_address', 'confidence_score')


class PhoneNumberContactSerializer(serializers.ModelSerializer):
    number = serializers.CharField()
    ISD_code = serializers.CharField()

    original_number = serializers.CharField()
    formatted_number = serializers.CharField()
    type = serializers.CharField()
    confidence_score = serializers.IntegerField()

    class Meta:
        model = PhoneNumberContact
        fields = ('id', 'number', 'ISD_code', 'original_number', 'formatted_number', 'type', 'confidence_score')


class EmailInfoSerializer(serializers.ModelSerializer):
    email_to = serializers.CharField()
    email_body = serializers.CharField()
    email_reply_to = serializers.CharField()
    email_signature = serializers.CharField()
    email_form = serializers.CharField()
    email_subject = serializers.CharField()
    email_cc = serializers.CharField()

    class Meta:
        model = EmailInfo
        fields = (
            'id', 'email_to', 'email_body', 'email_reply_to', 'email_signature', 'email_form', 'email_subject',
            'email_cc',)


class WebSiteSerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    url = serializers.URLField()

    class Meta:
        model = WebSite
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    # emails = EmailContactSerializer()
    # phone_numbers = PhoneNumberContactSerializer()
    email_info = EmailInfoSerializer()
    web_sites = WebSiteSerializer()

    class Meta:
        model = ContactInfo
        fields = '__all__'
