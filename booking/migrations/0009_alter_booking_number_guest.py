# Generated by Django 3.2.16 on 2023-01-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_number_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_guest',
            field=models.CharField(choices=[('3', '3'), ('1', '1'), ('7', '7'), ('6', '6'), ('5', '5'), ('2', '2'), ('4', '4')], default=2, max_length=2),
        ),
    ]
