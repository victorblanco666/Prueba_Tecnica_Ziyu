# Instrucciones para ejecutar el proyecto 

# Requisitos:

# Tener Python Instalado en la Maquina Local 

# 1- Crear entorno virtural para poder instalar las tecnologías Django necesarias:

# python -m venv venv 
# cd venv/Scripts
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process Ejecutar en caso de activate/deactivate no funcione 
# activate/deactivate Comandos para activar y desactivar el entorno virtual 
# cd .. 
# cd .. 

# 2- Instalar dependencias para el proyecto:

# pip install -r requirements.txt 

# 3- Ejecutar comando para iniciar servidor local:
# python manage.py runserver 

# 4- Abrir la aplicacion:
# Ctrl+Click en el enlace entregado Ej: "http://127.0.0.1:8000" para abrir la aplicación web

# Rutas del proyecto:

# http://127.0.0.1:8000/  --> Vista solicitar servicio
# http://127.0.0.1:8000/empresa --> Vista para ver pedidos, asignar jardineros y moniterar estado de los pedidos asignados 
# http://127.0.0.1:8000/jarinero/Indicar Id Del Jardinero ej: http://127.0.0.1:8000/jarinero/3  --> Vista para que un jardinero vea y administre sus pedidos 
# http://127.0.0.1:8000/confirmacion/Token de Seion Ej: http://127.0.0.1:8000/confirmacion/a4f4f1ce-4b03-4781-a3bd-70a1ef93c986/                                                            --> Hacer click en el enlace para ver el el estado del servicio solicitado y confirmar satisfaccion 
