from django import forms
from .models import OffersModel

class OfferForm(forms.ModelForm):    
    offer_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    offer_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    offer_maxvalue = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control'}))
    offer_minvalue = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control'}))
    offer_discount = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control'}))   
    
    class Meta:
        model = OffersModel
        fields = "__all__"
       