# Generated by Django 4.1.7 on 2023-03-15 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='select_doctor',
            field=models.ForeignKey(default="", on_delete=django.db.models.deletion.CASCADE, to='app_hospital_system.adddoctor'),
            preserve_default=False,
        ),
    ]
