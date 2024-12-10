from django.shortcuts import render, redirect
from .models import Blog
from .forms import Blogforms

# Create your views here.

def index (request):
    return render(request, 'app_blogs/index.html')

def blogs_list (request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'app_blogs/blog_list.html', context)

def blogs_create(request):
    form = Blogforms(request.POST)  

    if request.method == 'POST' and form.is_valid():
        form.save() 
        return redirect('app_blogs: blogs_create')
    else: 
        form = Blogforms()
        context = {'form': form}

    return render(request, 'app_blogs/blog_create.html', context)
    