from urllib.request import parse_keqv_list

from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .forms import PhoneForm, BrandSearchForm
from .models import Phone
from .serializer import PhoneSerializer



class PhoneByBrandReportView(APIView):
    def get(self, request, brand):
        data = Phone.objects.filter(brand__name__iexact=brand)
        serializer = PhoneSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SameBrandCountryAndPhoneCountryReportView(APIView):
    def get(self, request):
        data = Phone.objects.filter(brand__nationality=F("country_made"))
        serializer = PhoneSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



def addPhones(request):
    if request.method == 'GET':
        form = PhoneForm()
        return render(request, 'phones/addPhones.html', {"form":form})
    elif request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            try :
                Phone.objects.create(**form.cleaned_data)
                return HttpResponse("Created")
            except Phone.AlreadyExists:
                return HttpResponse("Already Exists")
        else:
            return HttpResponse("Error")

def redirectToSearchBrandPhone(request):
    if request.method == 'GET':
        form = BrandSearchForm()
        return render(request, 'phones/searchBrandPhone.html', {"form":form})
    elif request.method == 'POST':
        form = BrandSearchForm(request.POST)
        name = form.data['name']
        return HttpResponseRedirect(f"/phone/api/v1/brands/{name}/phones/")

class SearchPhoneModelMixin(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

