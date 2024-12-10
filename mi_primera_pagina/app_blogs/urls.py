from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_blogs'

urlpatterns = [
    path ('index/', views.index, name= 'index'),
    path('listar_blogs/', views.listar_blogs, name ='listar_blogs'),
    path('blogs_create/', views.blogs_create, name = 'blogs_create'),
]