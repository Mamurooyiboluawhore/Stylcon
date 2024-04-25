from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.views import APIView
# Create your views here.


class SearchView(APIView):
    '''
        a class that handles search functionality
    '''
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        products = Product.objects.filter(name_icontains=query).order_by('-createdat')

        serializer = self.serializer_class(products, many=True, context={'request': request})

        response = {
            'products': serializer.data,
            'query': query
        }
        return Response(response, status=status.HTTP_200_OK)