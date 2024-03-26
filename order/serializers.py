from rest_framework import serializers
from .models import Order


class OrderSerializers(serializers.ModelSerializer):
    """
        Order seializers class;
        serializes and deserializes data
    """
    class Meta:
        model = Order
        fields = ('id', 'customer', 'product', 'quantity')