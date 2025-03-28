import pygame

from random import randint

pygame.init()

ANCHURA_VENTANA = 600
ALTURA_VENTANA = 600

COLOR_FONDO = (255, 255, 250)
PANTALLA = pygame.display.set_mode((ALTURA_VENTANA, ANCHURA_VENTANA))

# buleano de gestión del bucle
PARAR_JUEGO = False

# Variables COHETE
XX_COHETE = 210
YY_COHETE = 300
ALTURA_COHETE = 32
ANCHURA_COHETE = 32
MOVIMIENTO_XX_COHETE = 0

# Variables PLANETAS
XX_PLANETA = randint(30, 130)
YY_PLANETA = 20
ALTURA_PLANETA = 111
ANCHURA_PLANETA = 80
XX_ENTRE_PLANETAS = 350
YY_ENTRE_PLANETA = 125
VELOCIDAD_PLANETAS = 2

# Puntos y otros
PUNTOS = 0
FUENTE = pygame.font.Font(None, 24)
MARCADOR = FUENTE.render("0 puntos", 1, (255, 0, 0))

# IMAGES
IMG_COHETE = pygame.image.load("img/COHETE.png")
IMG_PLANETA_IZQUIERDO = pygame.image.load("img/PLANETA.png")
IMG_PLANETA_DERECHO = pygame.image.load("img/PLANETA.png")

pygame.display.set_caption("PRIMER JUEGO")

while not PARAR_JUEGO:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                PARAR_JUEGO = True
            if event.key == pygame.K_RIGHT:
                MOVIMIENTO_XX_COHETE = 4
        elif event.type == pygame.KEYUP:
            MOVIMIENTO_XX_COHETE = -4

        if XX_COHETE < -10 or XX_COHETE > ALTURA_VENTANA:
            PARAR_JUEGO = True

    PANTALLA.fill(COLOR_FONDO)

    PANTALLA.blit(IMG_PLANETA_IZQUIERDO, (XX_PLANETA, YY_PLANETA))
    PANTALLA.blit(IMG_PLANETA_DERECHO, (XX_PLANETA + XX_ENTRE_PLANETAS, YY_PLANETA + YY_ENTRE_PLANETA))

    YY_PLANETA = YY_PLANETA + VELOCIDAD_PLANETAS

    if YY_PLANETA > ANCHURA_VENTANA:
        XX_PLANETA = randint(55, 150)
        YY_PLANETA = 25
        PUNTOS = PUNTOS + 1
        MARCADOR = FUENTE.render(str(PUNTOS) + " puntos", 1, (255, 0, 0))

    # PLANETA IZQUIERDO COLISION
    PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_X = XX_PLANETA + ALTURA_PLANETA
    PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_Y = YY_PLANETA + ANCHURA_PLANETA

    if PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_X > XX_COHETE:
        if PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_Y > YY_COHETE:
            if PUNTO_INFERIOR_DERECHO_PRIMER_PLANETA_Y < YY_COHETE + ANCHURA_COHETE:
                PARAR_JUEGO = True

    # PLANETA DERECHO COLISION
    PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_X = XX_PLANETA + XX_ENTRE_PLANETAS
    PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_Y = YY_PLANETA + \
        YY_ENTRE_PLANETA + ANCHURA_PLANETA

    if XX_COHETE + ALTURA_COHETE > PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_X:
        if XX_COHETE < PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_Y:
            if XX_COHETE + ANCHURA_COHETE > PUNTO_INFERIOR_IZQUIERDO_SEGUNDO_PLANETA_Y:
                PARAR_JUEGO = True

    XX_COHETE = XX_COHETE + MOVIMIENTO_XX_COHETE
    PANTALLA.blit(MARCADOR, (20, 580))
    PANTALLA.blit(IMG_COHETE, (XX_COHETE, YY_COHETE))
    pygame.display.update()