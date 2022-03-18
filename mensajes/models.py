from django.db import models
from django.forms import ValidationError


class Mensajes(models.Model):

    def validate_name(value):
        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)
        if length < 3:
            raise ValidationError(('Sé que no existe un nombre tan corto. 😆 Jajaja. Ingresa tu nombre completo. 😁'))

    nombre_contacto = models.CharField(max_length=100, validators=[validate_name])

    def validate_length(value):
        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)
        if length > 10:
            raise ValidationError(('Este número de telefóno es mayor a 10 números. Ingresa sólo 10 números.'))
        elif length < 10:
            raise ValidationError(('Este número de telefóno es menor a 10 números. Ingresa sólo 10 números.'))

    numero_telefono = models.PositiveBigIntegerField(validators=[validate_length])

    email = models.EmailField(blank=True, null=True)

    def validate_message(value):
        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)
        if length < 5:
            raise ValidationError(('El mensaje es muy corto. 👎 Detalla un poco más el motivo de tu mensaje.'))

    mensaje = models.TextField(validators=[validate_message])

    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_contacto


    class Meta:
        db_table = 'mensaje'
        managed = True
        verbose_name = 'mensaje'
        verbose_name_plural = 'mensajes'