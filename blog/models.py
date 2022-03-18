from ast import mod
from django.db import models
from django.forms import CharField
import uuid
import os
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Categorias(models.Model):
    
    categoria = models.CharField(max_length=25, primary_key=True)
    
    class Meta:
        db_table = 'categoria'
        managed = True
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.categoria
        
class Posts(models.Model):
    
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name="categoria_post")
    
    def get_file_path(instance, filename):
        """ Function for valid is unique """

        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('photos/', filename)

    photo = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    
    title_fb = models.CharField(max_length=50)
    
    title = models.CharField(max_length=100, primary_key=True)
    
    descripcion = models.CharField(max_length=255)
    
    contenido = models.TextField()
    
    slug = models.SlugField(unique=True, null=True, blank=False)
    
    autor = models.CharField(max_length=20, default="BrunoOrozco")
    
    fecha = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('posts', args=[str(self.slug)])

    def __str__(self):
        return self.slug
    
    class Meta:
        db_table = 'post'
        managed = True
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return 
    instance.slug = slugify(instance.title)

pre_save.connect(set_slug, sender=Posts)
        