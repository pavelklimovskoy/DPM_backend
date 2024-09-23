from django.db import models


class Salary(models.Model):
    amount = models.IntegerField()
    symbol = models.CharField(max_length=256)
    currency = models.CharField(max_length=256)
    unit = models.CharField(max_length=256)
    text = models.TextField()


class WorkedPeriod(models.Model):
    total_experience_month = models.IntegerField()
    total_experience_year = models.FloatField()
    total_experience_range = models.CharField()


class WorkInfo(models.Model):
    current_salary = models.OneToOneField(Salary, on_delete=models.CASCADE)
    expected_salary = models.OneToOneField(Salary, on_delete=models.CASCADE)

    experience = models.TextField()
    current_employer = models.CharField(254)
    job_profile = models.CharField()

    worked_period = models.OneToOneField(WorkedPeriod, on_delete=models.CASCADE)

    gap_period = models.IntegerField()
    average_stay = models.IntegerField()
    longest_stay = models.IntegerField()