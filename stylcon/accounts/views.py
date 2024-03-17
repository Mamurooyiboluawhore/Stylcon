from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializers
from rest_framework import status


class RegisterUserView(GenericAPIView):
    serializer_class=UserRegisterSerializers

    def post(self, request):
        user = request.data
        serializer =self.serializer_class(data=user)
        if serializer.is_valid():
            serializer.save()
            users=serializer.data
            response= {
                'message': f'welcome {users.first_name}!!',
                'data': users,
                'status_code': 201
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

