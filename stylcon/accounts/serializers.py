from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User


User = get_user_model()


class UserRegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(max_length=50, min_length=4, write_only=True)
    password2=serializers.CharField(max_length=50, min_length=5, write_only=True)

    class Meta:
        fields = ['email','first_name', 'last_name', 'password', 'password2']
    
        model = User


    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("passwords do not match")
        return attrs   
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email']
            first_name = validated_data.get('first_name')
            last_name = validated_data.get('last_name')
            password = validated_data.get('password')
        )
        return user
