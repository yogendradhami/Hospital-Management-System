# Generated by Django 4.1.7 on 2023-04-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0025_contactus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
