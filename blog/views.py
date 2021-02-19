from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all().order_by('-fecha_publicacion')
    context = {
        "blogs":blogs
    }
    return render(request, 'blog/blog.html', context)

def detail_blog(request, slug):
    blogs = Blog.objects.filter(slug=slug)
    context = {
        "blogs":blogs
    }
    return render(request, 'blog/detail-blog.html', context)