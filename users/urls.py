from django.urls import path
from .views import LogInView,register,LogOutView,UpdateView,Profil,LoginApiView,RegisterApiView,UserView,UserPost

app_name='users'
urlpatterns = [
    path('login/',LogInView.as_view(),name='login'),
    path('register/',register,name='register'),
    path('logout/',LogOutView.as_view(),name='logout'),
    path('update/<int:id>/', UpdateView.as_view(), name="update"),
    path('profil/<int:pk>/', Profil.as_view(), name="profil"),


    # api
    path('login_api/',LoginApiView.as_view(),name='login_api'),
    path('register_api/',RegisterApiView.as_view(),name='register'),
    path('users_api/',UserView.as_view(),name='user'),

    path('post/<int:id>/',UserPost.as_view(),name='user_post')
]
