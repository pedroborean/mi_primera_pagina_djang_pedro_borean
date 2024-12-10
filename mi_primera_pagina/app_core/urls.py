from django.urls import path
from . import views

app_name = 'app_core'

urlpatterns = [
    path ('index/', views.index, name = 'index')
]
