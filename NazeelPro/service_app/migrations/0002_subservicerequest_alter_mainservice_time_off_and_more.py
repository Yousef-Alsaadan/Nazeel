# Generated by Django 4.1.7 on 2023-06-20 13:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0014_remove_guest_all_remove_guest_is_active_and_more'),
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_delivered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest_app.room')),
                ('sub_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.subservice')),
            ],
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_off',
            field=models.DateTimeField(default=timezone.now()),
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_on',
            field=models.DateTimeField(default=timezone.now()),
        ),
        migrations.DeleteModel(
            name='OrderItm',
        ),
    ]
