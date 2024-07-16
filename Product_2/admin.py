from django.contrib import admin

# Register your models here.
from Product_2.models import productmodel_2


class productmodel_2Admin(admin.ModelAdmin):
    list_display = ["product_2_name", "product_2_img1", "product_2_img2","product_2_price","product_2_dis","product_2_active"]    

admin.site.register(productmodel_2,productmodel_2Admin)