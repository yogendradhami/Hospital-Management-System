# Generated by Django 4.1.7 on 2023-03-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specializaion', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='addmedicine',
            name='first_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]