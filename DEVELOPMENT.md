# Documentación Técnica del Desarrollo de Asteroids Game

## Visión General de la Arquitectura

Este documento describe la arquitectura y decisiones técnicas detrás del juego Asteroids, implementado en Python con Pygame. El juego sigue un diseño orientado a objetos con un enfoque en la composición de componentes.

## Estructura del Proyecto

```
asteroids-game/
│
├── main.py              # Punto de entrada, contiene el bucle principal del juego
├── constants.py         # Constantes globales usadas en todo el juego
├── circleshape.py       # Clase base abstracta para objetos circulares
├── player.py            # Implementación de la nave del jugador
├── asteroids.py         # Implementación de los asteroides
├── shot.py              # Implementación de los proyectiles
├── asteroidfield.py     # Generador de asteroides
├── README.md            # Documentación general del proyecto
├── INSTALL.md           # Guía de instalación con UV
├── GAMEPLAY.md          # Manual detallado del juego
└── DEVELOPMENT.md       # Este documento
```

## Diagrama de Clases

```
CircleShape (Base abstracta)
├── Player
├── Asteroid
└── Shot
```

## Descripción de Componentes

### CircleShape (circleshape.py)

Esta es la clase base abstracta que proporciona funcionalidad común para todos los objetos del juego:

- Hereda de `pygame.sprite.Sprite` para integración con grupos de sprites
- Propiedades básicas: posición, velocidad, radio
- Métodos abstractos: `draw()`, `update()`
- Implementa detección de colisiones circular con `collides_with()`

```python
def collides_with(self, other):
    distance = self.position.distance_to(other.position)
    return distance <= self.radius + other.radius
```

### Player (player.py)

Representa la nave controlada por el jugador:

- Hereda de `CircleShape`
- Implementa control de rotación y movimiento
- Maneja entrada del teclado en `update()`
- Implementa el sistema de disparo con temporizador de recarga
- Dibuja la nave como un triángulo

### Asteroid (asteroids.py)

Representa los asteroides que el jugador debe evitar y destruir:

- Hereda de `CircleShape`
- Implementa movimiento lineal
- Implementa la mecánica de división con `split()`
- Los asteroides divididos tienen:
  - Radio más pequeño
  - Velocidad aumentada (20% más rápida)
  - Dirección alterada (±20-50 grados)

### Shot (shot.py)

Representa los proyectiles disparados por el jugador:

- Hereda de `CircleShape`
- Movimiento simple en línea recta
- Se dibuja como un círculo pequeño relleno

### AsteroidField (asteroidfield.py)

Genera asteroides en el campo de juego:

- No es un objeto visible, solo generador
- Crea asteroides en posiciones aleatorias
- Controla la tasa de generación con una variable de tiempo

## Bucle Principal del Juego (main.py)

El bucle del juego sigue un patrón clásico:

1. Procesar eventos de entrada
2. Actualizar el estado del juego
3. Comprobar colisiones
4. Renderizar

Todas las entidades del juego se organizan en grupos de sprites para facilitar la gestión:
- `updateable`: Objetos que necesitan actualizarse cada frame
- `drawable`: Objetos que necesitan dibujarse
- `asteroids`: Específicamente los asteroides para comprobar colisiones
- `shots`: Proyectiles para comprobar colisiones

## Detección de Colisiones

Implementamos dos tipos de colisiones:

1. **Nave-Asteroide**: Termina el juego
2. **Proyectil-Asteroide**: Destruye/divide el asteroide y el proyectil

## Patrones de Diseño Utilizados

1. **Patrón Componente**: Reutilización de la funcionalidad de colisión a través de la clase base `CircleShape`
2. **Patrón Observer simplificado**: Los grupos de sprites actúan como observadores para las actualizaciones y el renderizado
3. **Game Loop**: Patrón clásico de bucle de juego para gestionar actualización y renderizado

## Decisiones Técnicas

### Por qué usar detección de colisiones circular

La detección de colisiones circular se eligió por:
- Simplicidad de implementación
- Eficiencia computacional
- Precisión suficiente para la jugabilidad deseada

Aunque la nave es visualmente un triángulo, usar un círculo para las colisiones proporciona una buena aproximación sin la complejidad de la detección de colisiones polígono-polígono.

### Sistema de Coordenadas y Movimiento

- Utilizamos un sistema de coordenadas cartesiano donde el origen (0,0) está en la esquina superior izquierda
- Las rotaciones siguen la convención matemática estándar (sentido antihorario)
- Usamos vectores (`pygame.Vector2`) para posición y velocidad, facilitando operaciones vectoriales

### Gestión del Tiempo

El juego utiliza un paso de tiempo delta para:
- Asegurar que el movimiento sea consistente independientemente de la velocidad de fotogramas
- Facilitar la implementación de temporizadores (como el enfriamiento de disparos)

```python
dt = fps / 1000.0  # Convierte milisegundos a segundos
```

## Consideraciones de Rendimiento

- La detección de colisiones es O(n*m) donde n es el número de proyectiles y m el número de asteroides
- No se implementa particionamiento espacial ya que la cantidad de objetos es relativamente pequeña
- El renderizado es simple y eficiente, utilizando primitivas de Pygame

## Áreas de Mejora Potencial

1. **Particionamiento espacial**: Para optimizar la detección de colisiones con muchos objetos
2. **Sistema de físicas más avanzado**: Añadir conceptos como masa y momento
3. **Implementación de patrones más formales**: Como el patrón Entity-Component-System
4. **Optimización de renderizado**: Técnicas como dirty rectangles para actualización parcial de pantalla

## Consideraciones para el Futuro

- **Arquitectura de plugins**: Para añadir nuevas características sin modificar el código base
- **Sistema de eventos**: Para desacoplar la lógica del juego
- **Serialización de estado**: Para guardar/cargar partidas
- **Refactorización a arquitectura MVC**: Separar mejor la lógica del juego, representación visual y control

## Recursos de Aprendizaje

Si estás interesado en aprender más sobre los conceptos utilizados:

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Game Programming Patterns](https://gameprogrammingpatterns.com/)
- [Nature of Code](https://natureofcode.com/) (para física básica)
- [Red Blob Games](https://www.redblobgames.com/) (tutoriales excelentes sobre matemáticas para juegos)