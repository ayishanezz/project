from django.shortcuts import render
from .serializers import ProductModelSerializer,OrderModelSerializer
from account.models import Products,Orders
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ProductModelViewSet(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductModelSerializer

class OrderModelViewSet(ModelViewSet):
    queryset=Orders.objects.all()
    serializer_class=OrderModelSerializer