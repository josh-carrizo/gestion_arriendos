from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    TIPO_USUARIO = [
        ('Arrendatario', 'Arrendatario'),
        ('Arrendador', 'Arrendador')
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.tipo_usuario}"

class Inmueble(models.Model):
    TIPO_INMUEBLE = [
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela')
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    metros_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    metros_totales = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE)
    precio_mensual = models.DecimalField(max_digits=12, decimal_places=2)
    arrendador = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='propiedades')

    def __str__(self):
        return f"{self.nombre} - {self.tipo_inmueble} en {self.comuna}"