from rest_framework import serializers

from phones.models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        depth = 2
        fields = '__all__'
