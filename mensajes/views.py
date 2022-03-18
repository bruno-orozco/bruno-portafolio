from django.shortcuts import render, redirect
from django.http.response import *
from mensajes.models import *
from django.db.models import *
from mensajes.forms import *

from django.core.mail import send_mail

from django.conf import settings

def contacto(request):

    data = {
        'form': formularioMensaje()
    }


    if request.method == 'POST':

        formulario = formularioMensaje(data=request.POST)
        if formulario.is_valid():



            formulario.save()
            data["mensaje"] = "Tu mensaje fue enviando correctamente. Pronto me comunicaré contigo."

        else:
            data["form"] = formulario


    return render(request, 'contacto.html', data)