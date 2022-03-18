from django.contrib import admin

from mensajes.models import *



@admin.register(Mensajes)
class Mensajes(admin.ModelAdmin):

    list_display = (
        'nombre_contacto',
        'numero_telefono',
        'email',
        'mensaje',
    )
