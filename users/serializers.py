from rest_framework import serializers

class LogIn(serializers.Serializer):
    username=serializers.CharField(max_length=100,min_length=20)
    password=serializers.CharField(min_length=4)