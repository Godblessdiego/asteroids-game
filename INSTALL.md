# Guía de Instalación de Asteroids Game usando UV

Esta guía te ayudará a instalar y ejecutar el juego de Asteroides utilizando UV, una herramienta moderna para gestión de entornos virtuales y dependencias en Python.

## Requisitos Previos

- Python 3.8 o superior
- Acceso a la línea de comandos (Terminal en macOS/Linux, Command Prompt o PowerShell en Windows)
- Git (opcional, para clonar el repositorio)

## Instalación de UV

UV es una alternativa rápida a pip y venv, escrita en Rust. Para instalar UV:

### En macOS/Linux:

```bash
curl -fsSL https://github.com/astral-sh/uv/releases/latest/download/uv-installer.sh | bash
```

### En Windows:

```powershell
powershell -c "irm https://github.com/astral-sh/uv/releases/latest/download/uv-installer.ps1 | iex"
```

## Obtener el Juego

### Opción 1: Clonar el repositorio (si tienes Git):

```bash
git clone https://github.com/Godblessdiego/asteroids-game.git
cd asteroids-game
```

### Opción 2: Descargar el código fuente:

1. Visita https://github.com/Godblessdiego/asteroids-game
2. Haz clic en "Code" y luego "Download ZIP"
3. Extrae el archivo ZIP y navega a la carpeta extraída

## Configuración del Entorno con UV

1. Abre una terminal en el directorio del juego (asteroids-game)

2. Crea un entorno virtual:

```bash
uv venv
```

3. Activa el entorno virtual:

### En macOS/Linux:

```bash
source .venv/bin/activate
```

### En Windows:

```powershell
.venv\Scripts\activate
```

4. Instala las dependencias necesarias:

```bash
uv pip install pygame
```

## Ejecutar el Juego

Una vez que hayas completado la instalación, puedes ejecutar el juego con:

```bash
python main.py
```

## Solución de Problemas

### Error: "No module named 'pygame'"

Si obtienes este error, asegúrate de que:
1. Has activado correctamente el entorno virtual
2. Has instalado pygame usando `uv pip install pygame`

### Error: "pygame.error: No available video device"

Este error puede ocurrir en entornos sin interfaz gráfica. Si estás utilizando un servidor remoto o WSL sin configuración gráfica, necesitarás configurar un servidor X.

### Rendimiento lento

Si el juego se ejecuta lentamente:
1. Cierra otras aplicaciones que consuman muchos recursos
2. Verifica que tu sistema cumple con los requisitos mínimos

## Notas Adicionales

- UV es significativamente más rápido que pip tradicional y venv, lo que facilita la configuración rápida de entornos para proyectos como este.
- Para actualizar pygame en el futuro: `uv pip install --upgrade pygame`
- Para crear un archivo de requisitos: `uv pip freeze > requirements.txt`

## Desinstalación

Para eliminar el entorno virtual, simplemente elimina la carpeta `.venv` del directorio del proyecto.

Para más información sobre UV, visita: https://github.com/astral-sh/uv