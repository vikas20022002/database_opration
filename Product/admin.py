from django.contrib import admin

# Register your models here.
from Product.models import ProductModel


class productmodelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductModel,productmodelAdmin)