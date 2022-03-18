from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from personal_profile import views as portafolio
from blog import views as posts
from mensajes import views as formulario
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

sitemaps = {
    'posts': PostsSitemaps,
}

urlpatterns = [
    path('', portafolio.index, name="index"),
    
    path('posts/', portafolio.aboutme, name="posts"),
    
    path('posts/<slug:slug>/', posts.PostsView.as_view() , name="posts"),
    path('contacto/', formulario.contacto, name="contacto"),
    path('admin/', admin.site.urls),
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

