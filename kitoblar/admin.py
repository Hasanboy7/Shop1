from django.contrib import admin
from .models import Tillar,Kitob,Comment
# Register your models here.

class Kitoblar(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=['name']

admin.site.register(Kitob,Kitoblar)
admin.site.register(Tillar)
admin.site.register(Comment)
