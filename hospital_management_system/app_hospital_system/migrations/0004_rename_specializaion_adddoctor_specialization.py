# Generated by Django 4.1.7 on 2023-03-16 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0003_drug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adddoctor',
            old_name='specializaion',
            new_name='specialization',
        ),
    ]
