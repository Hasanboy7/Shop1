from .models import Tillar

def catigory(request):
    return {'catigory':Tillar.objects.all()}