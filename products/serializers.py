from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    '''
        serializers all products
    '''
    class Meta:
        model = Product
        fields = '__all__'