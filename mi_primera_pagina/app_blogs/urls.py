from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_blogs'

urlpatterns = [
    path ('index/', views.index, name= 'index'),
    path('blogs_list/', views.blogs_list, name ='blog_list'),
    path('blogs_create/', views.blogs_create, name = 'blogs_create'),
]