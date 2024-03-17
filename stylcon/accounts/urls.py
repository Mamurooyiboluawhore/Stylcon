from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import RegisterUserView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterUserView.as_view(), name='register')
]