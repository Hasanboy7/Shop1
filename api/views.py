from django.shortcuts import render
from rest_framework.response import Response
from kitoblar.models import Tillar,Kitob
from .serializers import SerializerTillar,SerializerObject
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.custom_permission import IsAdminOrReadOnliy
# Create your views here.

class ViewTillar(APIView):
    permission_classes=(IsAdminOrReadOnliy,)
    def get(self,request):
        tillar=Tillar.objects.all()
        serilizer=SerializerTillar(tillar,many=True)
        return Response(serilizer.data)
    
class ViewCatigory(APIView):
    def get(self,request,id):
        tillaroject=Tillar.objects.get(id=id)
        catioryobject=tillaroject.til.all()
        serilizer=SerializerObject(catioryobject,many=True)
        return Response(serilizer.data)

class ViewCatigoryUpdate(APIView):
    serializer_class=SerializerTillar
    def get(self,request,id):
        tillaroject=Tillar.objects.get(id=id)
        serilizer=SerializerTillar(instance=tillaroject)
        return Response(serilizer.data)
    def put(self,request,id):
        kitob=Kitob.objects.get(id=id)
        result=request.data
        serilizer=SerializerTillar(instance=kitob,data=result)

        if serilizer.is_valid(raise_exception=True):
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    def patch(self,request,id):
        kitob=Kitob.objects.get(id=id)
        result=request.data
        serilizer=SerializerTillar(instance=kitob,data=result,partial=True)

        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data)

class ViewKitoblar(APIView):
    def get(self,request):
        kitob=Kitob.objects.all()
        serilizer=SerializerObject(kitob,many=True)
        return Response(serilizer.data)
    
class ViewKitob(APIView):
    serializer_class=SerializerObject
    def get(self,request,id):
        kitob=Kitob.objects.get(id=id)
        serilizer=SerializerObject(instance=kitob)
        return Response(serilizer.data)
    
    def put(self,request,id):
        kitob=Kitob.objects.get(id=id)
        result=request.data
        serilizer=SerializerObject(instance=kitob,data=result)

        if serilizer.is_valid(raise_exception=True):
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    def patch(self,request,id):
        kitob=Kitob.objects.get(id=id)
        result=request.data
        serilizer=SerializerObject(instance=kitob,data=result,partial=True)

        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data)
    
    def delete(self,request,id):
        kitob=Kitob.objects.get(id=id)
        kitob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)