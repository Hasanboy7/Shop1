from django.urls import path
from .views import ViewTillar,ViewCatigory,ViewKitoblar,ViewKitob,ViewCatigoryUpdate,CommentCreateView
app_name='api'
urlpatterns = [
    # path('tillar/',ViewTillar.as_view(),name='tillar'),
    # path('tillar/<int:id>/',ViewCatigory.as_view(),name='catigory'),
    # path('tillar_update/<int:id>/',ViewCatigoryUpdate.as_view(),name='catigoryupdate'),
    path('posts/',ViewKitoblar.as_view(),name='kitonlar'),
    path('post/<int:id>/',ViewKitob.as_view(),name='kitob'),

    path('comment_create/',CommentCreateView.as_view(),name='create'),
]
