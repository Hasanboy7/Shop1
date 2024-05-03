from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from kitoblar.models import Kitob

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100,min_length=4)
    password=serializers.CharField(min_length=4)
    
    def validate(self, attrs):
        username=attrs.get('username')
        password=attrs.get('password')
        
        user = authenticate(username=username,password=password)
        if user is None: 
            data = {
                "statuc":False,
                "messages":"User not found"
            }
            raise ValidationError(data)
        
        attrs['user']=user

        return attrs
    
    def to_representation(self, instance):
        user=instance['user']
        refresh = RefreshToken.for_user(user)
        data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        return data
    
class RegisterSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=150,min_length=4)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=50,required=True)
    confirm_password=serializers.CharField(max_length=50,required=True)


    def validate(self, attrs):
        password=attrs.get('password')
        confirm_password=attrs.get('confirm_password')

        if confirm_password !=password:
            data={
                "status":False,
                "messages":"Parollar bir-biriga mos tushmadi"
            }
            raise ValidationError(data)
        
        return attrs
        
    def validate_username(self,username):
        if username.startswith('@') or username.startswith('!'):
            data={
                "status":False,
                "messages":"Username is not valid"
            }
            raise ValidationError(data)
        
        return username
    
    def create(self, validated_data):
        username=validated_data['username']
        email=validated_data['email']
        password=validated_data['password']
        confirm_password=validated_data['confirm_password']

        user=User()

        user.username=username
        user.email=email
        user.set_password(password)
        user.save()
        return user
    
    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        data = {
                "status":True,
                "messages":"User regestred successfully",
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        return data



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__' #['first_name','last_name','email','img','age','body']

class PostUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Kitob
        fields='__all__'


