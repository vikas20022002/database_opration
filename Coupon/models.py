from django.db import models

# Create your models here.


class CouponModel(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_title = models.CharField(max_length=30)
    coupon_code = models.CharField(max_length=30)
    coupon_date = models.DateField()
    coupon_noofuse = models.IntegerField()
    coupon_active = models.CharField(max_length=5)
    coupon_description = models.CharField(max_length=50)


    class Meta:
        db_table = 'tbl_coupon'