from django.db import models


class EmailContact(models.Model):
    email_address = models.EmailField(
        default=""
    )
    confidence_score = models.IntegerField(
        default=0
    )


class PhoneNumberContact(models.Model):
    number = models.CharField(
        default="",
        max_length=128
    )
    ISD_code = models.CharField(
        default="",
        max_length=128
    )

    original_number = models.CharField(
        default="",
        max_length=128
    )
    formatted_number = models.CharField(
        default="",
        max_length=128
    )
    type = models.CharField(
        default="",
        max_length=128
    )
    confidence_score = models.IntegerField(default=0)


class EmailInfo(models.Model):
    email_to = models.CharField(
        default=""
    )
    email_body = models.CharField(
        default=""
    )
    email_reply_to = models.CharField(
        default=""
    )
    email_signature = models.CharField(
        default=""
    )
    email_form = models.CharField(
        default=""
    )
    email_subject = models.CharField(
        default=""
    )
    email_cc = models.CharField(
        default=""
    )


class WebSite(models.Model):
    type = models.CharField(
        default="",
        max_length=512
    )
    url = models.URLField(
        default=""
    )


class ContactInfo(models.Model):
    emails = models.ForeignKey(EmailContact, on_delete=models.CASCADE)
    phone_numbers = models.ForeignKey(PhoneNumberContact, on_delete=models.CASCADE)
    email_info = models.OneToOneField(EmailInfo, on_delete=models.CASCADE)
    web_sites = models.ForeignKey(WebSite, on_delete=models.CASCADE)
