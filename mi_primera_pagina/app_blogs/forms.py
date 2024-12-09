from django import forms
from .models import Blog

class Blogforms (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'autor', 'contenido']