from django.contrib import admin

from blog.models import *



@admin.register(Categorias)
class Categorias(admin.ModelAdmin):

    list_display = (
        'categoria',
    )
    
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    
    
admin.site.unregister(Posts)
admin.site.register(Posts, PostsAdmin)
    