from django.urls import path
from . import views

app_name = 'visitas'

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('empresa/', views.empresa, name='empresa'),
    path('asignar/<int:solicitud_id>/', views.asignar_jardinero, name='asignar_jardinero'),
    path('confirmacion/<uuid:token>/', views.confirmacion_cliente, name='confirmacion_cliente'),
    path('jardinero/<int:jardinero_id>/', views.jardinero_view, name='jardinero_view'),
    path('jardinero/iniciar/<int:solicitud_id>/', views.iniciar_servicio, name='iniciar_servicio'),
    path('jardinero/finalizar/<int:solicitud_id>/', views.finalizar_servicio, name='finalizar_servicio'),
]
