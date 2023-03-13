# Generated by Django 4.1.7 on 2023-03-13 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0002_adddoctor_addmedicine_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'app_department',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'app_doctor',
            },
        ),
        migrations.CreateModel(
            name='BookAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('appointment_date', models.DateField()),
                ('message', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hospital_system.department')),
            ],
        ),
    ]
