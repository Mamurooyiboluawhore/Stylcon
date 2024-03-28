from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.ModelSerializer):
    """
    Order serializers class;
    Serializes and deserializes data
    """
    class Meta:
        model = Order
        fields = ('id', 'customer', 'product', 'quantity')

class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Order create serializer class;
    Used to validate the incoming data before saving it in the database
    """
    class Meta:
        model = Order
        fields = ('product', 'name', 'created', 'quantity', 'subtotal', 'email', 'address', 'modified', 'postalCode', 'city', 'country', 'user')
        extra_kwargs = {
            'id': {'read_only': True},
            'created': {'read_only': True},
            'modified': {'read_only': True},
            'customer': {'read_only': True},  
            'subtotal': {'required': False},  
        }
