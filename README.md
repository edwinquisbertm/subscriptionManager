# Subscription Manager

Sistema de gestión de suscripciones, este sistema ayudara a la empresas que tienen un modelo de negocio por suscripción el poder gestionar a sus clientes, planes, pedidos y pagos.

## Autor

- [@edwinquisbertm](https://github.com/edwinquisbertm)

## Instalación

- Clonamos el Repositorio

```bash
git clone https://github.com/edwinquisbertm/subscriptionManager.git
```

- Ingresamos a la carpeta "subscriptionManager"

```bash
    cd subscriptionManager
```

- Creamos un entorno virtual

```bash
  python -m venv venv
```
- Inicializamos el entorno virtual

En Windows
```bash
  source venv/Script/activate
```
En Linux
```bash
  source venv/bin/activate
```

- Instalamos las dependencias

```bash
  pip install -r requirements.txt
```
- Creamos la Base de Datos

```bash
  python manage.py migrate
```

- Creamos un super usuario para gestionar la Administración

```bash
  python manage.py createsuperuser
```

- Iniciamos la aplicación con

```bash
  python manage.py runserver
```

## Rutas
- Home
```bash
http://127.0.0.1:8000/
```
- administracion de DJango
```bash
http://127.0.0.1:8000/admin
```