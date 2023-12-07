from django.db import models


class SegregatedSkillModel(models.Model):
    skill_type = models.CharField()
    skill = models.CharField(unique=True)
    ontology = models.CharField()
    alias = models.CharField()
    formatted_name = models.CharField()
    evidence = models.CharField()
    last_used = models.CharField()
    experience_in_months = models.CharField()


class SkillInfoModel(models.Model):
    skill_block = models.TextField()
    skill_keywords = models.TextField()

    segregated_skill = models.ManyToManyField(SegregatedSkillModel)
