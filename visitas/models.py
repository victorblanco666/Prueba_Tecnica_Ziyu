import uuid
from django.db import models

class Solicitud(models.Model):
    TIPO_SERVICIO_CHOICES = [
        ('poda', 'Poda'),
        ('corte_cesped', 'Corte de césped'),
        ('limpieza', 'Limpieza y mantenimiento'),
        ('otros', 'Otros'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('asignada', 'Asignada'),
        ('confirmada', 'Confirmada'),
        ('en_proceso', 'En proceso'),          # Nuevo: cuando el jardinero inicia
        ('pendiente_evaluacion', 'Pendiente de evaluación'), # Nuevo: tras finalizar
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    nombre_cliente = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    tipo_servicio = models.CharField(max_length=30, choices=TIPO_SERVICIO_CHOICES, default='otros')
    disponibilidad_horaria = models.CharField(max_length=120, blank=True)
    metros_cuadrados = models.PositiveIntegerField()
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='pendiente')
    jardinero_asignado = models.CharField(max_length=200, null=True, blank=True)
    hora_asignada = models.DateTimeField(null=True, blank=True)
    token_confirmacion = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Nuevos campos
    calificacion = models.PositiveIntegerField(null=True, blank=True)
    foto_cliente = models.ImageField(upload_to='solicitudes_fotos/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.tipo_servicio} ({self.estado})"

class Jardinero(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
