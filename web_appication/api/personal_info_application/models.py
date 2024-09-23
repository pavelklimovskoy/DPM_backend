from django.db import models

from api.country_application.models import Country

from api.location_application.models import LocationModel


class NameModel(models.Model):
    """
    Модель для описания имени пользователя
    """
    full_name = models.CharField(max_length=128)
    titled_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    formatted_name = models.CharField(max_length=128)

    confidence_score = models.IntegerField(default=0)


class LanguageModel(models.Model):
    """
    Модель для описания языка
    """
    language = models.CharField(max_length=128)
    language_code = models.CharField(max_length=8)


class AddressModel(models.Model):
    """
    Описание адреса проживания
    """
    street = models.CharField(max_length=256)

    location = models.OneToOneField(LocationModel, on_delete=models.DO_NOTHING)

    zip_code = models.CharField(max_length=256)

    formatted_address = models.CharField(max_length=256)

    type = models.CharField(max_length=256)

    confidence_score = models.IntegerField()


class PersonalInfoModel(models.Model):
    """
    Описание персональной информации о пользователе
    """
    name = models.OneToOneField(NameModel, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=8)

    father_name = models.CharField()
    mother_name = models.CharField()

    martial_status = models.CharField()
    nationality = models.CharField()

    language_known = models.ForeignKey(LanguageModel, on_delete=models.DO_NOTHING)

    hobbies = models.TextField()

    objectives = models.TextField()
    achievements = models.TextField()

    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)

    resume_language = models.OneToOneField(LanguageModel, on_delete=models.DO_NOTHING, related_name="resume_lang")
    resume_country = models.OneToOneField(Country, on_delete=models.DO_NOTHING)

    address = models.ForeignKey(AddressModel, on_delete=models.DO_NOTHING)
