from django.shortcuts import render
from django.db.models import Q

from blog.models import *

def index(request):

    return render(request, 'index.html')

def aboutme(request):
    
    search = request.GET.get("search")
    
    categorias_view = Categorias.objects.all() 
    
    posts_view = Posts.objects.all().order_by('-fecha')
    
    if search:
        posts_view = Posts.objects.filter(
            Q(title__icontains = search) |
            Q(contenido__icontains = search)            
        ).distinct()

    
    return render(request, 'posts.html', {'categoria': categorias_view,
                                            'posts': posts_view})

def skills(request):

    return render(request, 'skills.html')

def portafolio(request):

    return render(request, 'portafolio.html')

def contacto(request):

    return render(request, 'contacto.html')

