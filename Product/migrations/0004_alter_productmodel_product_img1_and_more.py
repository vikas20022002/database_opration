# Generated by Django 5.0.6 on 2024-06-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_productmodel_product_img1_productmodel_product_img2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_img1',
            field=models.CharField(default='abc.jpg', max_length=100),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_img2',
            field=models.CharField(default='abc.jpg', max_length=100),
        ),
    ]
