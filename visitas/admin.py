from django.contrib import admin
from .models import Solicitud,Jardinero

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_cliente', 'tipo_servicio', 'estado', 'created_at')
    list_filter = ('estado', 'tipo_servicio')
    search_fields = ('nombre_cliente', 'direccion')
    readonly_fields = ('created_at', 'token_confirmacion')


@admin.register(Jardinero)
class JardineroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'disponible')
    list_editable = ('disponible',)
