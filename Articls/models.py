from django.db import models

# Create your models here.

class AricalModel(models.Model):
    artical_id = models.AutoField(primary_key=True)
    artical_title = models.CharField(max_length=30)
    artical_description = models.CharField(max_length=50)
    artical_active = models.CharField(max_length=5)
    artical_authors = models.CharField(max_length=20)
    artical_date = models.CharField(max_length=20)
    artical_quote = models.CharField(max_length=30)

    class Meta:
        db_table = 'tbl_artical'
