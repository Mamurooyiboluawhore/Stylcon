from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    '''
        Retrieve all products from the database.
    '''
    def get(self, request):
        try:
            products = Product.objects.all()
            serializers = ProductSerializers(products, many=True)
            response = {
                'message': 'List of all Products',
                'status': status.HTTP_200_OK,
                'data': serializers.data
            }
            return Response(response, status=status.status.HTTP_200_OK)
        except Exception as e:
            response = {
                'error': str(e),
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk)
            serializer = ProductSerializers(product)
            response = {
                'message': 'Get one product',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
            return Response(response, status=status.status.HTTP_200_OK)
        except Exception as e:
            response = {
                'error': str(e),
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ProductDetailView(APIView):
    def post (self, request):
        '''
        an endpoint for creating products
        '''
        try:
            serializer = ProductSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save
                response = {
                    'message': 'Product added successfully',
                    'status': status.HTTP_201_CREATED,
                    'data': serializer.data
                }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                'error': str(e),
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, id):
        '''
        an endpoint for updating products
        '''
        try:
            product = Product.objects.get(id)
            serializer = ProductSerializers(product)
            if serializer.is_valid():
                serializer.save()
                response={
                    'message': 'Product successfully updated',
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
        
    def delete(self, request, pk):
        '''
        
        '''
        try:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            response = {
                'message': 'Product successfully deleted',
                'status': status.HTTP_204_NO_CONTENT,
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            response = {
                'error': str(e),
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
                



        


# Create your views here.
