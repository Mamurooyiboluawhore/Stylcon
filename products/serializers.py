from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    '''
        serializers all products
    '''
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'image', 'updated_at', 'created_at' ]
