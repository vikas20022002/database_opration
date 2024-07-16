from django.contrib import admin

# Register your models here.
from Offers.models import OffersModel


class OfferAdmin(admin.ModelAdmin):
    list_display = ["offer_name", "offer_description", "offer_maxvalue","offer_minvalue","offers_full_discount"]
    list_filter = ["offer_discount"]
admin.site.register(OffersModel, OfferAdmin)