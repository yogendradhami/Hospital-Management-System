# Generated by Django 4.1.7 on 2023-03-16 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0002_bookappointment_select_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=299)),
                ('specification', models.TextField()),
                ('cost', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app_drug',
            },
        ),
    ]
