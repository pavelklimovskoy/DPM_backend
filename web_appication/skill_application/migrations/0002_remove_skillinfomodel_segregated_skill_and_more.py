# Generated by Django 4.2.3 on 2023-08-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillinfomodel',
            name='segregated_skill',
        ),
        migrations.AddField(
            model_name='skillinfomodel',
            name='segregated_skill',
            field=models.ManyToManyField(to='skill_application.segregatedskillmodel'),
        ),
    ]
