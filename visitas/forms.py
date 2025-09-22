from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['nombre_cliente', 'direccion', 'tipo_servicio', 'disponibilidad_horaria', 'metros_cuadrados']

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['foto_cliente', 'calificacion']
        widgets = {
            'calificacion': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
