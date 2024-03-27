from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializers
from rest_framework import status
import json


class OrderList(APIView):
    """
    Retrieve all orders from the database.
    """

    def get(self, request, format=None):
        """
        Get all orders from the database.
        """
        try:
            orders = Order.objects.all()
            serializer = OrderSerializers(orders, many=True)
            response = {
                'message': 'list of all orders',
                'status': status.HTTP_200_OK,
                'data': serializer.data
                }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'error': str(e),
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

