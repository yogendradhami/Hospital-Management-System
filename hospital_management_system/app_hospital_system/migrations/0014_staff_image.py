# Generated by Django 4.1.7 on 2023-03-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0013_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='', upload_to='static/img/staff/'),
            preserve_default=False,
        ),
    ]
