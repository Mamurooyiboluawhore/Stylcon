from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError, ErrorDetail
from rest_framework import status

from .models import Catalogue
from .serializers import CatalogueSerializers



class CatalogueAPIViews(APIView):
    def get(self, request):
        try:
            catalogue = Catalogue.objects.all()
            serializer = CatalogueSerializers(catalogue)
            response = {
                'message': "list of all items in catalogue",
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'message': "Internal Server Error",
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }

            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            catalogue = Catalogue.objects.all()
            serializer = CatalogueSerializers(catalogue)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'message': 'Catalogue successfully created',
                    'status': status.HTTP_201_CREATED,
                    'data': serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except ValueError as e:
            response = {
                'error': str(e),
                'message': 'Internal server error',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR

            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, pk, request):

        try:
            catalogue = self.get_objects(pk)
            serializer = CatalogueSerializers(catalogue, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'message': 'Catalogue successfully updated',
                    'status': status.HTTP_200_OK,
                    'data': serializer.data
                }

                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            pass
        pass

    def delete(self, pk, request):
        try:
            catalogue = self.get_objects_or_404(Catalogue, pk)
            catalogue.delete()
            response = {
                'message': 'Catalogue successfully delete',
                'status': status.HTTP_204_NO_CONTENT
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            data = {
                "error_message": f"An error occurred while removing a product review: {str(e)}",
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)