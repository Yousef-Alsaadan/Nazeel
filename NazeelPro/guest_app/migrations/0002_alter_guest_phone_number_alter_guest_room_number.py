

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guest',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]
