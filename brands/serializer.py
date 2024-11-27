from rest_framework import serializers

from brands.models import Brand, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class BrandSerializer(serializers.ModelSerializer):
    nationality = serializers.StringRelatedField()
    class Meta:
        model = Brand
        # depth = 1
        fields = ("name", "nationality")
