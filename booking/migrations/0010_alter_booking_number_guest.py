# Generated by Django 3.2.16 on 2023-01-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_booking_number_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_guest',
            field=models.CharField(choices=[('7', '7'), ('1', '1'), ('2', '2'), ('6', '6'), ('3', '3'), ('5', '5'), ('4', '4')], default='2', max_length=2),
        ),
    ]
