# Generated by Django 5.0.6 on 2024-06-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_2', '0002_alter_productmodel_2_product_2_img1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel_2',
            name='product_2_dis',
            field=models.TextField(default='abc'),
        ),
    ]
