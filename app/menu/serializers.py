from rest_framework import serializers, viewsets
from .models import Product
from django_filters import rest_framework as filters

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductFilter(filters.FilterSet):
    name_like = filters.CharFilter(field_name='name', lookup_expr='icontains')
    category_like = filters.CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'category']
