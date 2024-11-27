from django.contrib import admin
from django.template.context_processors import request
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brand/', include("brands.urls")),
    path('phone/', include("phones.urls")),
]

