from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework import status
from .utils import generate_otp, send_mail
from rest_framework.views import APIView
from send_mail import send_plain_text_email
from .models import User
from datetime import timezone


class ValidateOTP(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        otp = request.data.get('otp', '')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        print(user.otp)  # Print the OTP for debugging purposes

        if user.otp == otp:
            # check if token has expired
            time_difference = max(user.created_at, user.updated_at)
            mins_difference = (
                timezone.now() - time_difference
            ).total_seconds() / 60
            if mins_difference > 2:
                response = {
                    "response_status": "error",
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "OTP token expired. Try again.",
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
            user.otp = None
            user.save()

            # Authenticate the user and create or get an authentication token
            # token, _ = Token.objects.get_or_create(user=user)

            return Response({'message': 'Account verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)

		

class ResendOtpView(APIView):
      def patch(self, request):
            """Resends a new OTP to the registered Email ID"""
            email = request.query_params.get('email')
            try:
                  user = User.objects.get(email=email)

            except User.DoesNotExist:
                  response = {'response_status':'error',
                              'status_code':status.HTTP_404_NOT_FOUND,
                              'message':'User does not exist'}
                  return Response(response, status=status.HTTP_404_NOT_FOUND)
            if user.otp is None:
                  response = {
                        'message': "Ypur account already verified"
                  }
                  return Response(response, status=status.HTTP_400_BAD_REQUEST)
            otp = generate_otp()
            user.otp=otp
            user.save()
            send_plain_text_email(message=otp, to_email=email, subject="this is your new otp")
            

            response ={
                  'message': 'new otp has been sent to your email!',
                  'status': status.HTTP_200_OK
            }
            return Response(response, status=status.HTTP_200_OK)
      

class RegisterUserView(GenericAPIView):
    serializer_class=UserRegisterSerializer

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

