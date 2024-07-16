from django.db import models

# Create your models here.
class OffersModel(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_name = models.CharField(max_length=30)
    offer_description = models.CharField(max_length=100)
    offer_maxvalue = models.DecimalField(max_digits=18,decimal_places=2)
    offer_minvalue = models.DecimalField(max_digits=18,decimal_places=2)
    offer_discount = models.DecimalField(max_digits=18,decimal_places=2)


    class Meta:
        db_table = 'tbl_offers'

    @property
    def offers_full_discount(self):
        return str(self.offer_discount) + "%"
    
    @property
    def offers_full_maxvalue(self):
        return str(self.offer_maxvalue) + "/-"

    @property
    def offers_full_minvalue(self):
        return str(self.offer_minvalue) + "/-"   