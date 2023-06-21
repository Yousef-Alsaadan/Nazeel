# Generated by Django 4.1.7 on 2023-06-20 21:44

from django.utils import timezone

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0002_subservicerequest_alter_mainservice_time_off_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='time_off',
            field=models.TimeField(default=timezone.now()),
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_on',
            field=models.TimeField(default=timezone.now()),
        ),
    ]
