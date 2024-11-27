from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import BrandForm, CountryForm, NationalitySearchForm
from .models import Brand, Country
from .serializer import BrandSerializer


class CountriesBrandViews(APIView):

    def get(self, request, country):
        data = Brand.objects.filter(nationality__name__iexact=country)
        serializer = BrandSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



def addCountry(request):
    if request.method == 'GET':
        form = CountryForm()
        return render(request, 'brands/addCountry.html', {"form":form})
    elif request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            Country.objects.create(**form.cleaned_data)
            return HttpResponse("Created")
        else:
            return HttpResponse("Error")


def addBrand(request):
    if request.method == 'GET':
        form = BrandForm()
        return render(request, 'brands/addBrand.html', {"form":form})
    elif request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            Brand.objects.create(**form.cleaned_data)
            return HttpResponse("Created")
        else:
            return HttpResponse("Error")

def redirectToCountriesBrand(request):
    if request.method == 'GET':
        form = NationalitySearchForm()
        return render(request, 'brands/redirectToCountryBrandView.html', {"form":form})
    elif request.method == 'POST':
        form = NationalitySearchForm(request.POST)
        name = form.data['name']
        return HttpResponseRedirect(f"/brand/api/v1/countries/{name}/brands/")

