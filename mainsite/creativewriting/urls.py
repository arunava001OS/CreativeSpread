from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('writing/',views.writing_index,name = "writing_index"),
    path('post_article/',views.post_article,name = "post_article"),
    path('register/',views.register,name = "register"),
    path('login/',views.Login,name = "login"),
    path('logout/',views.Logout,name = "logout"),
    path('',views.index,name = "index"),
]