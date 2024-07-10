# Generated by Django 4.1.13 on 2024-04-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0044_appointment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_information',
            name='consultation_fee',
            field=models.IntegerField(blank=True, default='None', null=True),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='dob',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='nid',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='report_fee',
            field=models.IntegerField(blank=True, default='None', null=True),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='visiting_hour',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]
