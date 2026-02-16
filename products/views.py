from rest_framework import generics, permissions, status
from rest_framework.response import Response 
from drf_spectacular.utils import extend_schema
from .serializers import ProductSerializer
from .models import Product

@extend_schema(tags=['Products'])
class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

@extend_schema(tags=['Products'])
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()