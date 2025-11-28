# Backend Python - Gestión de Personas

Este proyecto es una API REST construida con **Django** y **Django REST Framework** para la gestión de información de personas. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre entidades de tipo "Persona".

## Características

- Gestión de Personas con validación de tipos de documento (Cédula, TI, Pasaporte, etc.).
- API RESTful documentada y versionada.
- Configuración lista para desarrollo.

## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

- [Python](https://www.python.org/) (versión 3.8 o superior)
- [pip](https://pip.pypa.io/en/stable/) (gestor de paquetes de Python)
- [git](https://git-scm.com/) (para clonar el repositorio)

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1.  **Clonar el repositorio:**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd backendPython
    ```

2.  **Crear y activar un entorno virtual (Recomendado):**

    Es buena práctica usar un entorno virtual para aislar las dependencias.

    - En Linux/macOS:

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - En Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuración de Base de Datos

El proyecto utiliza SQLite por defecto, lo cual es ideal para desarrollo. Necesitas aplicar las migraciones para crear las tablas necesarias.

```bash
python manage.py migrate
```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

El servidor estará corriendo en `http://127.0.0.1:8000/`.

## Uso de la API

La API está disponible bajo el prefijo `/api/v1/`.

### Endpoints Principales

- **Listar y Crear Personas:** `GET /api/v1/personas/` | `POST /api/v1/personas/`
- **Detalle, Actualizar y Eliminar Persona:** `GET /api/v1/personas/<id>/` | `PUT /api/v1/personas/<id>/` | `DELETE /api/v1/personas/<id>/`

### Ejemplo de Creación (POST)

**URL:** `http://127.0.0.1:8000/api/v1/personas/`

**Body (JSON):**

```json
{
  "tipo_documento": "CC",
  "documento": "123456789",
  "nombres": "Juan",
  "apellidos": "Pérez",
  "hobbie": "Programar"
}
```

### Tipos de Documento Válidos

- `CC`: Cédula de Ciudadanía
- `TI`: Tarjeta de Identidad
- `CE`: Cédula de Extranjería
- `PAS`: Pasaporte
- `OTR`: Otro

## Estructura del Proyecto

- `config/`: Configuraciones globales del proyecto Django (settings, urls principales).
- `core/`: Aplicación principal que contiene la lógica del negocio (modelos, vistas, serializadores).
- `manage.py`: Utilidad de línea de comandos de Django.
