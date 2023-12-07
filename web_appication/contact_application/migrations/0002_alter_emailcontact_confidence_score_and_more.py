# Generated by Django 4.2.3 on 2023-08-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcontact',
            name='confidence_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='emailcontact',
            name='email_address',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_body',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_cc',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_form',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_reply_to',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_signature',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_subject',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='emailinfo',
            name='email_to',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='phonenumbercontact',
            name='ISD_code',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='phonenumbercontact',
            name='formatted_number',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='phonenumbercontact',
            name='number',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='phonenumbercontact',
            name='original_number',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='phonenumbercontact',
            name='type',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='website',
            name='type',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(default=''),
        ),
    ]