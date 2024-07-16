from django.db import models

# Create your models here.

class productmodel_2(models.Model):
    YES = 'YES'
    NO = 'NO'

    CONSENT_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    product_2_id = models.AutoField(primary_key=True)
    product_2_name = models.CharField(max_length=30)
    product_2_img1 = models.ImageField(upload_to ='product')
    product_2_img2 = models.ImageField(upload_to ='product')
    product_2_price = models.IntegerField()
    product_2_dis = models.TextField(default='abc')
    product_2_active = models.CharField(max_length=3, choices=CONSENT_CHOICES, default=YES)


    class Meta:
        db_table = 'tbl_product_2'

    @property
    def full_price(self):
        return "Rs." + str(self.product_price) + '/-'