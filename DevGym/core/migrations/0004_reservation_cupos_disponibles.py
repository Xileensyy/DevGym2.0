# Generated by Django 4.2.2 on 2023-06-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customuser_managers_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='cupos_disponibles',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
