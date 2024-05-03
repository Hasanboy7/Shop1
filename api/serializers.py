from rest_framework import serializers
from kitoblar.models import Tillar,Kitob,Comment

class SerializerTillar(serializers.ModelSerializer):
    
    class Meta:
        model=Tillar
        exclude=['id']

class SerializerObject(serializers.ModelSerializer):
    
    class Meta:
        model=Kitob
        exclude=['id']


class CommentCreate(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"
    


    