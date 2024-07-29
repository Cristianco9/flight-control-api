# Proyecto Flight API

## Descripción

Este proyecto es una API construida con Django para el control de un dron DJI Tello. Permite enviar comandos al dron para realizar acciones específicas como despegar, moverse y tomar fotografías. La API está diseñada para ser utilizada en aplicaciones de control de cultivos y procesamiento de imágenes.

## Requisitos

- Python 3.8 o superior
- Django 4.0 o superior
- Django REST Framework
- `djitellopy` (para controlar el dron DJI Tello)

## Instalación

Sigue estos pasos para clonar el proyecto, instalar las dependencias y configurarlo para su uso.

### 1. Clonar el Repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
```


### 2. Navega al directorio del proyecto clonado

```bash
    cd flight-control-api
```

### 3. Crea un entorno virtual

```bash
    python3 -m venv ~/.envs/flight_api_env
```

### 4. Activa el entorno virtual

En WSL o Unix:

```bash
    source ~/.envs/flight_api_env/bin/activate
```

### 5. Instalar las dependencias

```bash
    pip3 install -r requirements.txt
```

### 6. Ejecuta el servidor de desarrollo

```bash
    python3 manage.py runserver
```

El servidor se ejecutará en el puerto: `http://127.0.0.1:8000`.

### 7. Desactivar el entorno virtual

Para deshabilitar el entorno virtual del proyecto de Python ejecuta el comando:

```bash
    deactivate
```

## USO

Para controlar el dron, envía solicitudes POST a`http://127.0.0.1:8000/api/v1/test` con el comando deseado en el cuerpo de la solicitud. Ejemplo de cuerpo de solicitud:

```json
    {
        "command": "takeoff"
    }
```

## USO


## CONTRIBUCIÓN


## LICENCIA


## CONTACTO
