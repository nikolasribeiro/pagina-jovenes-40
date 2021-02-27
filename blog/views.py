from django.shortcuts import render
from .models import Blog, Categoria

# Create your views here.
def blog(request):

    lista_categorias    = []

    blogs = Blog.objects.all().order_by('-fecha_publicacion')
    categorias = Categoria.objects.all().values_list()
    
    for index, categoria in enumerate(categorias):
        lista_categorias.append(categorias[index])


    busqueda_usuario = request.POST.get('buscador-input')
    seleccion_de_categoria = request.GET.get('categoria')

    # Barra de busqueda
    if busqueda_usuario is not None:
        busqueda_usuario = busqueda_usuario.strip()
        
        # Checkea si la palabra clave es una categoria
        for elemento in lista_categorias:
            if busqueda_usuario.lower() == elemento[1].lower():
                blogs = Blog.objects.filter(categoria=elemento[0]).order_by('-fecha_publicacion')
            else:
                print("No existe categoria")
        else:
            blogs = Blog.objects.filter(titulo_blog=busqueda_usuario).order_by('-fecha_publicacion')
            print("Deberia de entrar aca si no entra en la lista_categorias")
    
    elif seleccion_de_categoria is not None:
        blogs = Blog.objects.filter(categoria=seleccion_de_categoria).order_by('-fecha_publicacion')
    else:
        blogs = Blog.objects.all().order_by('-fecha_publicacion')
    
    
    
    # Click en los links de categorias
    blog_categorias = Categoria.objects.all()

    context = {
        "blogs":blogs,
        "categorias":blog_categorias,
    }

    return render(request, 'blog/blog.html', context)



def detail_blog(request, slug):
    blogs = Blog.objects.filter(slug=slug)
    context = {
        "blogs":blogs
    }
    return render(request, 'blog/detail-blog.html', context)