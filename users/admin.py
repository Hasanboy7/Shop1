from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name']
    list_display_links=['username']

admin.site.register(User,UserAdmin)