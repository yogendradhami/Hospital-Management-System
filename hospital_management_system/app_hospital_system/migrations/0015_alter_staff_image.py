# Generated by Django 4.1.7 on 2023-03-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0014_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to='static/img/staff'),
        ),
    ]
