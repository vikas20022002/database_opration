# Generated by Django 5.0.6 on 2024-05-28 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_remove_employeemodel_employee_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemodel',
            old_name='employee_xender',
            new_name='employee_gender',
        ),
    ]
