# subscriptionManager
Sistema de Gestión de Suscripciones

## Instalación
python -m venv venv

source venv/Script/activate

pip install django

./manage.py migrate
./manage.py makemigrate

pip install requirements.txt

py manage.py createsuperuser

./manage.py runserver

# Descripción del Sistema de Gestión de Suscripciones
El sistema permite registrar a los clientes, establecer tipos de planes y gestionar los pagos.