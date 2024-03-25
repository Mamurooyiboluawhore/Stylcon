from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError, ErrorDetail
from rest_framework import status

from .models import Catalogue
from .serializers import CatalogueSerializers
# Create your views here.


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