# Generated by Django 5.0.6 on 2024-06-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offers', '0002_offersmodel_delete_employeemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offersmodel',
            name='offer_discount',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
