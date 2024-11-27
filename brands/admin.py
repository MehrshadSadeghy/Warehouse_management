from django.contrib import admin

from .models import Country, Brand

class CountryAdmin(admin.ModelAdmin):
    pass

class BrandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(Brand, BrandAdmin)
