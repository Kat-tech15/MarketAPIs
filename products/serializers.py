from rest_framework import serializers
from .models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'owner', 'type', 'name', 'price', 'image', 'is_available']