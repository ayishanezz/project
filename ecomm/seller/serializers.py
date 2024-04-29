from rest_framework import serializers
from account.models import Products,Orders


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields="__all__"