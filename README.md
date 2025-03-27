# bimestral_1
# PRIMER JUEGO - Explicación del Código

Este documento proporciona una explicación detallada, línea por línea, del código del juego desarrollado con Pygame.

```python
import pygame
Línea 1: Importa la librería Pygame, que es necesaria para crear juegos en Python.

Python

from random import randint
Línea 2: Importa la función randint del módulo random. Esta función se utilizará para generar números enteros aleatorios, por ejemplo, para la posición inicial de los planetas.

Python

pygame.init()

Línea 4: Inicializa todos los módulos importados de Pygame. Es un paso necesario antes de poder usar cualquier función de Pygame.

Python

ANCHURA_VENTANA = 600
ALTURA_VENTANA = 600

Líneas 6-7: Define dos constantes: ANCHURA_VENTANA y ALTURA_VENTANA, ambas con un valor de 600. Estas constantes determinarán las dimensiones de la ventana del juego.

Python

COLOR_FONDO = (255, 255, 250)
Línea 9: Define una constante llamada COLOR_FONDO como una tupla RGB (Rojo, Verde, Azul). En este caso, representa un color blanco ligeramente apagado.

Python

PANTALLA = pygame.display.set_mode((ALTURA_VENTANA, ANCHURA_VENTANA))
Línea 10: Crea la ventana del juego. pygame.display.set_mode() devuelve un objeto Surface que representa la ventana. Las dimensiones de la ventana se toman de las constantes ALTURA_VENTANA y ANCHURA_VENTANA.

Python

# buleano de gestión del bucle
PARAR_JUEGO = False

Línea 13: Define una variable booleana llamada PARAR_JUEGO y la inicializa en False. Esta variable controlará el bucle principal del juego; el juego continuará ejecutándose mientras PARAR_JUEGO sea False.

Python

# Variables COHETE
XX_COHETE = 210
YY_COHETE = 300
ALTURA_COHETE = 32
ANCHURA_COHETE = 32
MOVIMIENTO_XX_COHETE = 0

Líneas 16-20: Define variables relacionadas con el cohete del jugador:

XX_COHETE: Coordenada horizontal (eje X) de la posición del cohete. Inicialmente se establece en 210.
YY_COHETE: Coordenada vertical (eje Y) de la posición del cohete. Inicialmente se establece en 300.
ALTURA_COHETE: Altura del cohete (en píxeles).
ANCHURA_COHETE: Ancho del cohete (en píxeles).
MOVIMIENTO_XX_COHETE: Cantidad de píxeles que el cohete se moverá horizontalmente en cada fotograma. Inicialmente es 0 (sin movimiento).
Python

# Variables PLANETAS
XX_PLANETA = randint(30, 130)
YY_PLANETA = 20
ALTURA_PLANETA = 32
ANCHURA_PLANETA = 32
XX_ENTRE_PLANETAS = 350
YY_ENTRE_PLANETA = 125
VELOCIDAD_PLANETAS = 2

Líneas 23-29: Define variables relacionadas con los planetas (obstáculos):

XX_PLANETA: Coordenada horizontal del primer planeta (el de la izquierda). Su valor inicial se genera aleatoriamente entre 30 y 130.
YY_PLANETA: Coordenada vertical del primer planeta. Inicialmente se establece en 20.
ALTURA_PLANETA: Altura de los planetas (en píxeles).
ANCHURA_PLANETA: Ancho de los planetas (en píxeles).
XX_ENTRE_PLANETAS: Distancia horizontal entre el primer y el segundo planeta.
YY_ENTRE_PLANETA: Desplazamiento vertical del segundo planeta respecto al primero.
VELOCIDAD_PLANETAS: Cantidad de píxeles que los planetas se moverán verticalmente hacia abajo en cada fotograma.
Python

# Puntos y otros
PUNTOS = 0
FUENTE = pygame.font.Font(None, 24)
MARCADOR = FUENTE.render("0 puntos", 1, (255, 0, 0))

Líneas 32-35: Define variables relacionadas con la puntuación y el texto:

PUNTOS: Variable que almacena la puntuación actual del jugador. Inicialmente es 0.
FUENTE: Crea un objeto de fuente utilizando la fuente predeterminada de Pygame y un tamaño de 24 puntos.
MARCADOR: Renderiza el texto inicial del marcador ("0 puntos") utilizando la fuente definida, con el color rojo (255, 0, 0) y con antialiasing activado (el segundo argumento '1').
Python
Línea 62: Incrementa la coordenada vertical (YY_PLANETA) del primer planeta en la cantidad definida por VELOCIDAD_PLANETAS. Esto hace que los planetas se muevan hacia abajo.

Python

    if YY_PLANETA > ANCHURA_VENTANA:
        XX_PLANETA = randint(55, 150)
        YY_PLANETA = 25
        PUNTOS = PUNTOS + 1
        MARCADOR = FUENTE.render(str(PUNTOS) + " puntos", 1, (255, 0, 0))

Líneas 64-68: Comprueba si el primer planeta ha pasado la parte inferior de la ventana (YY_PLANETA > ANCHURA_VENTANA). Si es así:


Línea 65: Genera una nueva posición horizontal aleatoria para el primer planeta entre 55 y 150.

Línea 66: Restablece la posición vertical del primer planeta a 25 (apareciendo de nuevo en la parte superior).

Línea 67: Incrementa la puntuación (PUNTOS) en 1.

Línea 68: Vuelve a renderizar el texto del marcador con la nueva puntuación.


Python

    # PLANETA IZQUIERDO COLISION
    PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_X = XX_PLANETA + ALTURA_PLANETA
    PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_Y = YY_PLANETA + ANCHURA_PLANETA

    if PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_X > XX_COHETE:
        if PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_Y > YY_COHETE:
            if PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_Y < YY_COHETE + ANCHURA_COHETE:
                PARAR_JUEGO = True
Líneas 71-78: Lógica de detección de colisión con el planeta izquierdo:


Líneas 72-73: Calcula las coordenadas del punto inferior derecho del primer planeta.

Línea 75: Comprueba si el borde derecho del planeta está a la derecha del borde izquierdo del cohete.

Línea 76: Si la condición anterior es verdadera, comprueba si el borde inferior del planeta está por debajo del borde superior del cohete.

Línea 77: Si las condiciones anteriores son verdaderas, comprueba si el borde inferior del planeta está por encima del borde inferior del cohete. Si todas estas condiciones se cumplen, significa que ha habido una colisión, y se establece PARAR_JUEGO en True.
Nota: Esta lógica de colisión es una simplificación y podría no ser completamente precisa para todas las formas y orientaciones. Para una detección de colisiones más robusta, se suelen utilizar rectángulos de colisión (pygame.Rect) y la función colliderect().

Python

    # PLANETA DERECHO COLISION
    PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_X = XX_PLANETA + XX_ENTRE_PLANETAS
    PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_Y = YY_PLANETA + \
        YY_ENTRE_PLANETA + ANCHURA_PLANETA

    if XX_COHETE + ALTURA_COHETE > PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_X:
        if XX_COHETE < PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_Y:
            if XX_COHETE + ANCHURA_COHETE > PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_Y:
                PARAR_JUEGO = True
Líneas 81-89: Lógica de detección de colisión con el planeta derecho:

Líneas 82-84: Calcula las coordenadas del punto inferior izquierdo del segundo planeta.

Línea 86: Comprueba si el borde derecho del cohete está a la derecha del borde izquierdo del segundo planeta.

Línea 87: Si la condición anterior es verdadera, comprueba si el borde izquierdo del cohete está a la izquierda del borde inferior del segundo planeta.

Línea 88: Si las condiciones anteriores son verdaderas, comprueba si el borde derecho del cohete está a la derecha del borde inferior del segundo planeta. Si todas estas condiciones se cumplen, significa que ha habido una colisión, y se establece PARAR_JUEGO en True.
Nota: Al igual que con el planeta izquierdo, esta lógica de colisión es una simplificación.

Python

    XX_COHETE = XX_COHETE + MOVIMIENTO_XX_COHETE
    PANTALLA.blit(MARCADOR, (20, 580))
    PANTALLA.blit(IMG_COHETE, (XX_COHETE, YY_COHETE))
    pygame.display.update()
Líneas 91-94: Actualiza el estado del juego y dibuja los elementos en la pantalla:

Línea 91: Actualiza la posición horizontal del cohete sumando el valor de MOVIMIENTO_XX_COHETE.

Línea 92: Dibuja el texto del marcador (MARCADOR) en la posición (20, 580) de la ventana.

Línea 93: Dibuja la imagen del cohete (IMG_COHETE) en la posición actual (XX_COHETE, YY_COHETE).

Línea 94: Actualiza toda la pantalla para mostrar los cambios realizados en este fotograma. Sin esta línea, no verías ninguna actualización en la ventana del juego.
Python

pygame.quit()
Línea 96: Cuando el bucle principal del juego termina (porque PARAR_JUEGO se vuelve True), esta línea se ejecuta. pygame.quit() desinicializa todos los módulos de Pygame que fueron inicializados con pygame.init().
