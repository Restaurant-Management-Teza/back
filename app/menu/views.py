from rest_framework import viewsets, status
from .models import Product
from .serializers import ProductSerializer, ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def post(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

    def delete(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return response




