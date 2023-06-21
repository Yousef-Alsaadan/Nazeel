# Generated by Django 4.1.7 on 2023-06-20 13:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest_app', '0014_remove_guest_all_remove_guest_is_active_and_more'),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=100)),
                ('description_service', models.CharField(max_length=1000)),
                ('time_on', models.DateTimeField(default=timezone.now())),
                ('time_off', models.DateTimeField(default=timezone.now())),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('rating', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=100)),
                ('catogory', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('main_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.mainservice')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(blank=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest_app.guest')),
                ('sub_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.subservice')),
            ],
        ),
    ]
