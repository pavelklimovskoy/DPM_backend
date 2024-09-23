from django.db import models


class Employer(models.Model):
    employer_name = models.CharField()
    formatted_name = models.CharField()
    confidence_score = models.IntegerField()


class JobProfile(models.Model):
    title = models.CharField()
    formatted_name = models.CharField()
    alias = models.CharField()
    related_skills = models.CharField()
    confidence_score = models.IntegerField()


class Projects(models.Model):
    used_skills = models.CharField()
    project_name = models.CharField()
    team_size = models.IntegerField()


class ExperienceModel(models.Model):

    employer = models.OneToOneField(Employer, on_delete=models.CASCADE)

    job_profile = models.OneToOneField(JobProfile, on_delete=models.CASCADE)

    # location = models.OneToOneField()

    formatted_job_period = models.DateTimeField(auto_now=True)

    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)

    is_current_employer = models.BooleanField(default=False)

    job_description = models.CharField()

    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
