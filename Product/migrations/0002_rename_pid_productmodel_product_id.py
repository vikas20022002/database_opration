# Generated by Django 5.0.6 on 2024-05-27 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='pid',
            new_name='product_id',
        ),
    ]
