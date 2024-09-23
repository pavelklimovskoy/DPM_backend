# Generated by Django 4.2.3 on 2023-08-18 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill_application', '0001_initial'),
        ('cv_application', '0005_cvmodel_personal_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvmodel',
            name='skill_info',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='skill_application.skillinfomodel'),
            preserve_default=False,
        ),
    ]