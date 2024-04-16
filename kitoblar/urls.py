from django.urls import path
from .views import KitoblarView,KitobView,AddComment,Cart,AddKitobView,AddTilView,UpdatePlace,delete
app_name='kitob'

urlpatterns = [
    path('',KitoblarView.as_view(),name='kitoblar'),
    path('addkitob/',AddKitobView.as_view(),name='addkitob'),
    path('addtil/',AddTilView.as_view(),name='addtil'),
    path('kitob/<int:id>',KitobView.as_view(),name='kitob'),
    path('update/<int:pk>',UpdatePlace.as_view(),name='update'),
    path('add_comment/<int:id>',AddComment.as_view(),name='add_comment'),
    path('cart/<int:id>',Cart,name='cart_kitob'),
    path('delete/<int:pk>/',delete,name='delete'),
]
