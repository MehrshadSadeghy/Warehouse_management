from django.urls import path
from .views import addBrand, addCountry, redirectToCountriesBrand
from .views import CountriesBrandViews

urlpatterns = [
    path("ui/v1/countries/new/", addCountry, name="addCountry"),
    path("ui/v1/brands/new/", addBrand, name="addBrand"),
    path("api/v1/countries/<str:country>/brands/", CountriesBrandViews.as_view(), name="koreaBrand"),
    path("redirect/brand/country/", redirectToCountriesBrand, name="redirectToCountryBrandView"),
]
