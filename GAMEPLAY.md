# MANUAL DE JUEGO: ASTEROIDS

## INTRODUCCIÓN

Bienvenido a **Asteroids**, un clásico juego de arcade reimaginado en Python con Pygame. En este juego, tomas el control de una nave espacial triangular mientras navegas por un campo de asteroides peligroso. Tu misión es sobrevivir el mayor tiempo posible, destruyendo asteroides y evitando colisiones fatales.

## LA HISTORIA

Te encuentras pilotando una nave espacial en un sector remoto del espacio lleno de asteroides. Tu nave de exploración ha sido equipada con un cañón láser para defenderse. Tu objetivo es sobrevivir y limpiar la zona de asteroides para garantizar el paso seguro de naves futuras.

## OBJETIVOS DEL JUEGO

- **Objetivo principal**: Sobrevivir el mayor tiempo posible
- **Objetivo secundario**: Destruir asteroides para acumular puntos (funcionalidad que se implementará en versiones futuras)

## CONTROLES

| Tecla | Acción |
|-------|--------|
| W | Impulsar nave hacia adelante |
| S | Impulsar nave hacia atrás |
| A | Rotar nave en sentido antihorario |
| D | Rotar nave en sentido horario |
| ESPACIO | Disparar proyectil |

## ELEMENTOS DEL JUEGO

### La Nave
- Representada por un triángulo blanco
- Se mueve mediante propulsión: mantiene su velocidad en el espacio
- Puede disparar proyectiles a una velocidad limitada (cada 0.3 segundos)
- Colisiona con asteroides, lo que resulta en "Game Over"

### Asteroides
- Existen en tres tamaños: grande, mediano y pequeño
- Se mueven en trayectorias lineales a velocidad constante
- Cuando son impactados por un proyectil:
  * Asteroides grandes → Se dividen en 2 asteroides medianos
  * Asteroides medianos → Se dividen en 2 asteroides pequeños
  * Asteroides pequeños → Desaparecen
- Los asteroides más pequeños se mueven más rápido que sus predecesores

### Proyectiles
- Pequeñas esferas blancas que viajan en línea recta
- Se disparan en la dirección en que apunta la nave
- Desaparecen al impactar con un asteroide
- Tienen un tiempo de recarga de 0.3 segundos entre disparos

## MECÁNICAS DE JUEGO

### Física de Movimiento
El juego implementa una física básica de movimiento inercial:
- La nave mantiene su impulso al moverse
- Los asteroides se mueven a velocidad constante en línea recta
- No hay fricción en el espacio

### Sistema de Colisiones
Todas las colisiones se calculan utilizando detección de colisión circular:
- Cada objeto (nave, asteroides, proyectiles) tiene un radio asociado
- Se produce una colisión cuando la distancia entre los centros de dos objetos es menor o igual a la suma de sus radios

### División de Asteroides
Cuando un asteroide es impactado:
1. El asteroide original desaparece
2. Si no es un asteroide pequeño, se crean dos nuevos asteroides más pequeños
3. Los nuevos asteroides se mueven en direcciones que divergen de la trayectoria original
4. Los nuevos asteroides se mueven un 20% más rápido que el asteroide original

## ESTRATEGIAS

### Consejos para Principiantes
- Mantén espacio libre a tu alrededor para tener rutas de escape
- Dispara a los asteroides desde lejos para tener tiempo de evitar los fragmentos
- Usa el impulso hacia atrás (tecla S) para frenar cuando sea necesario
- Evita quedarte inmóvil en un punto

### Técnicas Avanzadas
- Utiliza el "disparo estratégico": destruye asteroides pequeños primero para reducir amenazas inmediatas
- Aprovecha la inercia para deslizarte entre grupos de asteroides mientras disparas
- Crea zonas seguras destruyendo grupos de asteroides en áreas específicas

## RENDIMIENTO DEL JUEGO

El juego funciona mejor en:
- Sistemas con al menos 4GB de RAM
- Cualquier CPU moderna (2015 en adelante)
- Cualquier tarjeta gráfica básica o integrada

## SOLUCIÓN DE PROBLEMAS COMUNES

### El juego se ejecuta lentamente
- Cierra otras aplicaciones que consuman recursos
- Verifica que tu sistema cumple con los requisitos mínimos
- Reinicia el juego y/o la computadora

### El juego se cierra inesperadamente
- Comprueba que tienes instalada la versión correcta de Python y Pygame
- Verifica que todos los archivos del juego están presentes y no han sido modificados

## DESARROLLO FUTURO

Características planeadas para futuras versiones:
- Sistema de puntuación
- Niveles de dificultad progresiva
- Efectos de sonido y música
- Vidas adicionales
- Powerups y mejoras para la nave
- Tablas de clasificación en línea

---

¡Buena suerte, piloto espacial! La supervivencia del sector depende de ti.