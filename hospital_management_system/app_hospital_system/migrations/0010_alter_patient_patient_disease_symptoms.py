# Generated by Django 4.1.7 on 2023-03-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0009_rename_patient_diease_symptoms_patient_patient_disease_symptoms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_disease_symptoms',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
