[README.md](https://github.com/urivarela09FI/Condomino_APP/files/13745702/README.md)

# Condomino - Aplicación de Gestión Comunitaria

## Descripción
Condomino es una aplicación web diseñada para gestionar comunidades. Permite a los usuarios registrarse, elegir su rol (administrador o vecino), y acceder a funciones específicas según su rol.

## Requisitos Previos
- Python 3.x instalado en tu sistema.
- Pip (administrador de paquetes de Python) instalado.

## Instalación
1. Clona o descarga el repositorio de GitHub:

    ```bash
    git clone https://github.com/urivarela09FI/Condomino_APP
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tu_repositorio
    ```

3. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En sistemas Unix/Linux
    # o
    .\venv\Scripts\activate  # En sistemas Windows
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración
1. Copia el archivo `.env.example` y renómbralo a `.env`:

    ```bash
    cp .env.example .env  # En sistemas Unix/Linux
    # o
    copy .env.example .env  # En sistemas Windows
    ```

2. Edita el archivo `.env` con tu configuración:

    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    ```

## Ejecución
1. Ejecuta la aplicación:

    ```bash
    flask run
    ```

2. Abre tu navegador y visita `http://localhost:5000`.

## Contribuciones
Si encuentras algún problema o tienes sugerencias para mejorar la aplicación, por favor, crea un "issue" en el repositorio.

## Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
