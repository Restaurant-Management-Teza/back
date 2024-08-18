from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer, ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


