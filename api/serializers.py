from rest_framework import serializers
from kitoblar.models import Tillar,Kitob

class SerializerTillar(serializers.ModelSerializer):
    
    class Meta:
        model=Tillar
        exclude=['id']

class SerializerObject(serializers.ModelSerializer):
    
    class Meta:
        model=Kitob
        exclude=['id']
        