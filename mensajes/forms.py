from django import forms
from django.forms.widgets import EmailInput
from .models import *




class formularioMensaje(forms.ModelForm):

    

    nombre_contacto = models.CharField(max_length=100)

    numero_telefono = models.PositiveBigIntegerField()

    email = models.EmailField()

    mensaje = models.TextField()

    class Meta:
            model = Mensajes
            fields = '__all__'
            labels = {
                "nombre_contacto": "Escribe tu nombre completo",
                "numero_telefono": "Escribe tu número telefónico",
            }
            widgets = {
                'numero_telefono' : forms.NumberInput(attrs={'type' : 'tel'}),
                'email' : forms.EmailInput(attrs={'placeholder' : 'opcional'}),
                'mensaje' : forms.TextInput(attrs={'class' : 'width'})
                }

    def clean_email(self):
        email = self.cleaned_data['email'] or None
        return email


