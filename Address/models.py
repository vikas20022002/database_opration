from django.db import models

# Create your models here.


class AddressModel(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_title = models.CharField(max_length=30)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30,default='')
    address_city = models.CharField(max_length=30)
    address_state = models.CharField(max_length=30)
    address_type = models.CharField(max_length=10)


    class Meta:
        db_table = 'tbl_address'