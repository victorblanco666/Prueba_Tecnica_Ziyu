from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .forms import EvaluacionForm, SolicitudForm
from .models import Solicitud, Jardinero

def cliente(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            messages.success(
                request,
                'Solicitud creada correctamente. '
                f'Guarda este enlace para ver tu confirmación: '
                f'{request.build_absolute_uri("/confirmacion/"+str(solicitud.token_confirmacion)+"/")}'
            )
            return redirect('visitas:cliente')
        else:
            messages.error(request, 'Hay errores en el formulario.')
    else:
        form = SolicitudForm()
    return render(request, 'visitas/cliente.html', {'form': form})

def empresa(request):
    solicitudes = Solicitud.objects.all().order_by('-created_at')
    jardineros = Jardinero.objects.filter(disponible=True)
    return render(request, 'visitas/empresa.html', {
        'solicitudes': solicitudes,
        'jardineros': jardineros
    })

def asignar_jardinero(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_id)
    if request.method == 'POST':
        jardinero_id = request.POST.get('jardinero_id')
        hora_asignada = request.POST.get('hora_asignada')
        if jardinero_id and hora_asignada:
            jardinero = get_object_or_404(Jardinero, pk=jardinero_id)
            solicitud.jardinero_asignado = jardinero.nombre
            solicitud.hora_asignada = hora_asignada
            solicitud.estado = 'asignada'
            solicitud.save()
            messages.success(request, f'Solicitud {solicitud.id} asignada a {jardinero.nombre}')
        else:
            messages.error(request, 'Debes seleccionar jardinero y hora.')
    return redirect('visitas:empresa')

def iniciar_servicio(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_id)
    if solicitud.estado == 'asignada':
        solicitud.estado = 'en_proceso'
        solicitud.save()
        messages.success(request, f"Servicio de la solicitud {solicitud.id} iniciado.")
    # Obtener el objeto Jardinero por nombre
    jardinero = get_object_or_404(Jardinero, nombre=solicitud.jardinero_asignado)
    return redirect('visitas:jardinero_view', jardinero_id=jardinero.id)

def finalizar_servicio(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_id)
    if solicitud.estado == 'en_proceso':
        solicitud.estado = 'pendiente_evaluacion'
        solicitud.save()
        messages.success(request, f"Servicio de la solicitud {solicitud.id} finalizado. Pendiente de evaluación del cliente.")
    # Obtener el objeto Jardinero por nombre
    jardinero = get_object_or_404(Jardinero, nombre=solicitud.jardinero_asignado)
    return redirect('visitas:jardinero_view', jardinero_id=jardinero.id)

def confirmacion_cliente(request, token):
    solicitud = get_object_or_404(Solicitud, token_confirmacion=token)
    if solicitud.estado == 'pendiente_evaluacion':
        if request.method == 'POST':
            form = EvaluacionForm(request.POST, request.FILES, instance=solicitud)
            if form.is_valid():
                solicitud.estado = 'completada'
                form.save()
                messages.success(request, 'Gracias por evaluar el servicio.')
                return redirect('visitas:confirmacion_cliente', token=token)
        else:
            form = EvaluacionForm(instance=solicitud)
        return render(request, 'visitas/confirmacion.html', {'solicitud': solicitud, 'form': form})
    return render(request, 'visitas/confirmacion.html', {'solicitud': solicitud})


def jardinero_view(request, jardinero_id):
    jardinero = get_object_or_404(Jardinero, pk=jardinero_id)
    solicitudes = Solicitud.objects.filter(jardinero_asignado=jardinero.nombre).order_by('-created_at')
    return render(request, 'visitas/jardinero.html', {
        'jardinero': jardinero,
        'solicitudes': solicitudes
    })