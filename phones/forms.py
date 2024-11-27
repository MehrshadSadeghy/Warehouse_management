from email.policy import default
from itertools import filterfalse

from django import forms

from phones.models import Phone, Brand, Country


class PhoneForm(forms.Form):
    brand = forms.ModelChoiceField(Brand.objects.all())
    phone_name = forms.CharField()
    price = forms.IntegerField()
    color = forms.CharField()
    screen_size = forms.DecimalField()
    status = forms.BooleanField(required=False)
    country_made = forms.ModelChoiceField(Country.objects.all())


class BrandSearchForm(forms.Form):
    name = forms.CharField()

