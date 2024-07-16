from django.db import models

# Create your models here.

class CityModel(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)
    city_img = models.CharField(max_length=100)
    state_id = models.ForeignKey('State.StateModel',db_column='state_id', on_delete=models.CASCADE,default='')


    class Meta:
        db_table = 'tbl_city'