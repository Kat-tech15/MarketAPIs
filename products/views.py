from rest_framework import generics, permissions, status
from rest_framework.response import Response 
from .serializers import ProductSerializer
from .models import Product

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()