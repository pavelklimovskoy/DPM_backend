# Generated by Django 4.2.3 on 2023-08-21 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassportDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField()),
                ('date_of_expire', models.CharField()),
                ('date_of_issue', models.CharField()),
                ('place_of_issue', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField()),
                ('license_no', models.CharField()),
                ('pan_no', models.CharField()),
                ('visa_status', models.CharField()),
                ('passport_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document_application.passportdetailmodel')),
            ],
        ),
    ]
