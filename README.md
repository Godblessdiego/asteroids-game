# Juego de Asteroides

Un juego de arcade clásico implementado en Python utilizando Pygame donde controlas una nave espacial y debes destruir asteroides mientras evitas chocar contra ellos.

## Descripción del Juego

En este juego de Asteroides, el jugador controla una nave triangular que puede rotar y moverse en un espacio bidimensional. El objetivo es sobrevivir el mayor tiempo posible mientras destruyes asteroides que aparecen aleatoriamente en la pantalla.

### Características Principales

- **Nave del jugador**: Una nave triangular que puede rotar y moverse hacia adelante y hacia atrás.
- **Asteroides**: Aparecen de forma aleatoria en el campo de juego con diferentes tamaños.
- **Sistema de disparo**: La nave puede disparar proyectiles para destruir asteroides.
- **Mecánica de división de asteroides**: Cuando un asteroide grande es impactado, se divide en dos asteroides medianos que se mueven más rápido. Los asteroides medianos se dividen en dos pequeños, y los pequeños desaparecen al ser impactados.
- **Colisiones realistas**: Implementación de detección de colisiones basada en círculos para todos los objetos del juego.
- **Control de cadencia de disparo**: Límite en la frecuencia de disparos para equilibrar la dificultad.

## Requisitos

- Python 3.6 o superior
- Pygame 2.0 o superior

## Instalación

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala Pygame utilizando pip:

```bash
pip install pygame
```

3. Clona este repositorio o descarga los archivos del juego.

## Cómo Ejecutar el Juego

1. Abre una terminal o línea de comandos.
2. Navega hasta el directorio donde se encuentra el juego.
3. Ejecuta el archivo principal:

```bash
python main.py
```

## Controles

- **W**: Mover la nave hacia adelante
- **S**: Mover la nave hacia atrás
- **A**: Rotar la nave en sentido antihorario
- **D**: Rotar la nave en sentido horario
- **Barra espaciadora**: Disparar proyectiles
- **Cerrar ventana**: Salir del juego

## Mecánicas del Juego

- La nave puede moverse libremente por la pantalla.
- Los asteroides aparecen desde los bordes de la pantalla.
- Si la nave choca contra un asteroide, el juego termina.
- Los disparos tienen un tiempo de enfriamiento para evitar disparos continuos.
- Los asteroides se dividen de la siguiente manera:
  - Asteroides grandes → 2 asteroides medianos
  - Asteroides medianos → 2 asteroides pequeños
  - Asteroides pequeños → Desaparecen

## Estructura del Código

- **main.py**: Punto de entrada del juego, contiene el bucle principal.
- **player.py**: Implementa la clase para la nave del jugador.
- **circleshape.py**: Clase base para objetos circulares con detección de colisiones.
- **asteroids.py**: Implementa la clase para los asteroides.
- **shot.py**: Implementa la clase para los proyectiles.
- **asteroidfield.py**: Maneja la generación de asteroides.
- **constants.py**: Contiene constantes utilizadas en todo el juego.

## Desarrollo

Este juego fue desarrollado como un proyecto educativo para demostrar conceptos de programación orientada a objetos y física básica en videojuegos utilizando Python y Pygame.
