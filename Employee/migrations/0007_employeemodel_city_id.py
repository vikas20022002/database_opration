# Generated by Django 5.0.6 on 2024-06-21 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('City', '0002_citymodel_state_id'),
        ('Employee', '0006_alter_employeemodel_employee_photo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='city_id',
            field=models.ForeignKey(db_column='state_id', default='', on_delete=django.db.models.deletion.CASCADE, to='City.citymodel'),
        ),
    ]
