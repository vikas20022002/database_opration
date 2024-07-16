from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_qty = models.IntegerField()
    product_img1 = models.CharField(max_length=100,default="abc.jpg")
    product_img2 = models.CharField(max_length=100,default="abc.jpg")
    product_price = models.DecimalField(max_digits=18, decimal_places=2)
    product_description = models.TextField(null = True)

    class Meta:
        db_table = 'tbl_product'

    @property
    def full_price(self):
        return "Rs." + str(self.product_price) + '/-'

    @property
    def total(self):
        return str(self.product_qty * self.product_price) + '/-'
