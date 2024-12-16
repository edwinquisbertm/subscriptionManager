# Subscription Manager

Sistema de gestión de suscripciones, este sistema ayudara a la empresas que tienen un modelo de negocio por suscripción el poder gestionar a sus clientes, planes, pedidos y pagos.

## Autor

- [@edwinquisbertm](https://github.com/edwinquisbertm)

## Instalación

Inicializamos un entorno virtual

```bash
  python -m venv venv

  source venv/Script/activate
ó
  source venv/bin/activate
  
```

Instalamos las dependencias

```bash
  pip install requirements.txt
```
Creamos la Base de Datos

```bash
  python manage.py migrate
```

Creamos un super usuario para gestionar la Base de Datos

```bash
  python manage.py createsuperuser
```

Iniciamos la aplicación con

```bash
  python manage.py runserver
```