# Generated by Django 3.2.9 on 2022-03-18 05:32

from django.db import migrations, models
import mensajes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contacto', models.CharField(max_length=100, validators=[mensajes.models.Mensajes.validate_name])),
                ('numero_telefono', models.PositiveBigIntegerField(validators=[mensajes.models.Mensajes.validate_length])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mensaje', models.TextField(validators=[mensajes.models.Mensajes.validate_message])),
                ('fecha', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'mensaje',
                'verbose_name_plural': 'mensajes',
                'db_table': 'mensaje',
                'managed': True,
            },
        ),
    ]
