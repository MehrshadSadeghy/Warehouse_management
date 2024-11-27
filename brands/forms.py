from django import forms

from .models import Brand, Country

class BrandForm(forms.Form):
    name = forms.CharField()
    nationality = forms.ModelChoiceField(Country.objects.all())

class CountryForm(forms.Form):
    name = forms.CharField()

class NationalitySearchForm(forms.Form):
    name = forms.CharField()