from django.shortcuts import render,redirect
from django.views.generic import ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import RegisterForm,LoginForm,UpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView 
from .serializers import LoginSerializer,RegisterSerializers,UserSerializers,PostUserSerializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from kitoblar.models import Kitob


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.info(request, "Registratsadan muffaqyatli o'ttingiz")
            return redirect('users:login')
    else:
        form = RegisterForm()
       
    return render(request, 'user/register.html', context={'form': form})

class LogInView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'user/login.html',context={'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Sayitga maffaqyatli tashrif buyurdingiz')
                return redirect('kitob:kitoblar')

        return render(request,'user/login.html',context={'form':form})


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.warning(request, 'Sayitdan chiqib ketingiz')
        return redirect('kitob:kitoblar')

class Profil(View):
    def get(self,request,pk):
        user_profil=User.objects.get(id=pk)
        return render(request,'user/profil.html',context={'user_profil':user_profil})
    
class UpdateView(LoginRequiredMixin,View):  
    def get(self,request,id):
        form=UpdateForm(instance=request.user)
        return render(request,'user/update.html',context={'form':form})
    def post(self,request,id):
        if request.method=='POST':
            form =UpdateForm(instance=request.user,data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                messages.warning(request,"Mufaqyatli O'zgartirildi")
                return redirect('kitob:kitoblar')

        return render(request, 'user/update.html', context={'form': form})
    







# serializers
    
class LoginApiView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

    def post(self,request):
        data=request.data
        serializes=LoginSerializer(data=data)
        serializes.is_valid(raise_exception=True)
        return Response(serializes.data,status=status.HTTP_200_OK)

class RegisterApiView(APIView):
    def post(self,request):
        data=request.data
        serilaziers=RegisterSerializers(data=data)
        serilaziers.is_valid(raise_exception=True)
        serilaziers.save()
        return Response(serilaziers.data,status=status.HTTP_201_CREATED)

class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserPost(APIView):
    def get(self,request,id):
        queryset=User.objects.get(id=id)
        user_post=Kitob.objects.filter(user=queryset)
        serializers=PostUserSerializers(data=user_post,many=True)
        serializers.is_valid(raise_exception=True)
        return Response(serializers.data)
    

        