from django.urls import path
from .views import addPhones, redirectToSearchBrandPhone, PhoneByBrandReportView, SameBrandCountryAndPhoneCountryReportView, SearchPhoneModelMixin

urlpatterns = [
    path("ui/v1/phones/new/", addPhones, name="addPhones"),
    path("ui/v1/search_by_brand/", redirectToSearchBrandPhone, name="searchBrand"),
    path("api/v1/brands/<str:brand>/phones/", PhoneByBrandReportView.as_view(), name="searchBrand"),
    path("api/v1/reports/same_brand_country_and_country_search/", SameBrandCountryAndPhoneCountryReportView.as_view(), name="same country"),
    path("api/v1/phone/<str:pk>/", SearchPhoneModelMixin.as_view, name="phone"),
]
