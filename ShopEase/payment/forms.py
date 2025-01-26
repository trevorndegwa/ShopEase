from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    fullname_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full name'}), required=True)
    email_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=True)
    address1_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=True)
    address2_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=True)
    country_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)
    county_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'County'}), required=False)
    city_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
    postalcode_shipping = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Postal Code'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = ['fullname_shipping', 'email_shipping', 'address1_shipping', 'address2_shipping', 'country_shipping', 'county_shipping', 'city_shipping', 'postalcode_shipping']
        exclude = ['user',]

