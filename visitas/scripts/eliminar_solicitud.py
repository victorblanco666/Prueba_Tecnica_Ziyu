
"""
Script para eliminar una solicitud por ID desde shell_plus de Django.

Uso:
1. Abre shell_plus:
    python manage.py shell_plus
2. Importa y ejecuta la función:
    from visitas.scripts.eliminar_solicitud import eliminar_solicitud
    eliminar_solicitud(x)  # Reemplaza 14 por el ID que quieras eliminar
"""

from visitas.models import Solicitud

def eliminar_solicitud(solicitud_id):
    """
    Elimina la solicitud con el ID proporcionado.

    Args:
        solicitud_id (int): ID de la solicitud a eliminar.

    Muestra mensaje de éxito o error si no existe la solicitud.
    """
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.delete()
        print(f"✅ Solicitud con ID {solicitud_id} eliminada correctamente.")
    except Solicitud.DoesNotExist:
        print(f"⚠️ No existe ninguna solicitud con ID {solicitud_id}.")
