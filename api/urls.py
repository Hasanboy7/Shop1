from django.urls import path
from .views import ViewTillar,ViewCatigory,ViewKitoblar,ViewKitob,ViewCatigoryUpdate
app_name='api'
urlpatterns = [
    path('tillar/',ViewTillar.as_view(),name='tillar'),
    path('tillar/<int:id>/',ViewCatigory.as_view(),name='catigory'),
    path('tillar_update/<int:id>/',ViewCatigoryUpdate.as_view(),name='catigoryupdate'),
    path('kitoblar/',ViewKitoblar.as_view(),name='kitonlar'),
    path('kitob/<int:id>/',ViewKitob.as_view(),name='kitob')
]
