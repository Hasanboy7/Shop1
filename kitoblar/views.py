from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Kitob,Tillar,Comment
from .forms import CommentForm,AddKitob,AddTilForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class KitoblarView(View):
    def get(self,request):
        kitoblar=Kitob.objects.all()
        catigory=Tillar.objects.all()
        search_query=request.GET.get('q',"")
        if search_query:
            kitoblar=kitoblar.filter(name__icontains=search_query)
        date={
            'kitoblar':kitoblar,
            'catigory':catigory,
            'search_query':search_query
        }
        return render(request,'home.html',context=date)
    
class KitobView(View):
    def get(self,request,id):
        kitob=Kitob.objects.get(id=id)
        form=CommentForm()
        return render(request,'detail.html',context={'kitob':kitob,'form':form})


class AddComment(LoginRequiredMixin,View):
    def post(self,request,id):
        place=Kitob.objects.get(id=id)
        form=CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                place=place,
                comment_text=form.cleaned_data['comment_text'],
                start_give=form.cleaned_data['start_give'],
            )
            return redirect(reverse('kitob:kitob',kwargs={'id':place.id}))
        return render(request,'detail.html',context={'kitob':place,'form':form})


def Cart(request,id):
    t=Tillar.objects.get(id=id)
    cart=t.til.all()
    return render(request,'home.html',context={'kitoblar':cart})

class AddKitobView(View):
    def get(self,request):
        form=AddKitob()
        return render(request,'addkitob.html',context={'form':form})
    def post(self,request):
        if request.method=='POST':
            form=AddKitob(data=request.POST)
            if form.is_valid():
                form.save()
            
                return redirect('kitob:kitoblar')
        return render(request,'addkitob.html',context={'form':form})
    
class AddTilView(View):
    def get(self,request):
        form=AddTilForm()
        return render(request,'addkitob.html',context={'form':form})
    def post(self,request):
        if request.method=='POST':
            form=AddTilForm(data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('kitob:kitoblar')
        return render(request,'addtil.html',context={'form':form})


class UpdatePlace(View):
    def get(self, request, pk):
        place_instance = Kitob.objects.get(id=pk)
        form = AddKitob(instance=place_instance)
        return render(request, 'update.html', context={'form': form})
    
    def post(self, request,pk):
        place_instance = Kitob.objects.get(id=pk)
        form = AddKitob(instance=place_instance, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Muvaffaqiyatli o'zgartirildi")
            return redirect('kitob:kitoblar') 
        return render(request, 'update.html', context={'forms': form})
    
def delete(request, pk):
    place_instance = get_object_or_404(Kitob, id=pk)
    place_instance.delete()
    return redirect('kitob:kitoblar')