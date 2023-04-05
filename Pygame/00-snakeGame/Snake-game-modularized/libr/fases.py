import pygame

from . import *


def veriFase(cobra):
    if variaveis.fase == 1:
        fase1()
    elif variaveis.fase == 2:
        fase2(cobra)
    elif variaveis.fase == 3:
        fase3(cobra)


def fase1():
    pygame.draw.line(variaveis.tela, (0, 200, 0), (10, 30), (630, 30))
    pygame.draw.line(variaveis.tela, (0, 200, 0), (10, 450), (630, 450))
    pygame.draw.line(variaveis.tela, (0, 200, 0), (10, 30), (10, 450))
    pygame.draw.line(variaveis.tela, (0, 200, 0), (630, 30), (630, 450))
    if variaveis.cobrax < 16:
        variaveis.cobrax = 626
    if variaveis.cobrax > 626:
        variaveis.cobrax = 16
    if variaveis.cobray < 36:
        variaveis.cobray = 446
    if variaveis.cobray > 446:
        variaveis.cobray = 36


def fase2(cobra):
    cima = pygame.draw.line(variaveis.tela, (200, 0, 0), (10, 30), (630, 30))
    baixo = pygame.draw.line(variaveis.tela, (200, 0, 0), (10, 450), (630, 450))
    esquerda = pygame.draw.line(variaveis.tela, (200, 0, 0), (10, 30), (10, 450))
    direita = pygame.draw.line(variaveis.tela, (200, 0, 0), (630, 30), (630, 450))
    if cobra.colliderect(cima) or cobra.colliderect(baixo) or cobra.colliderect(esquerda) or cobra.colliderect(direita):
        morte()


def fase3(cobra):
    cima = pygame.draw.line(variaveis.tela, (0, 0, 0), (10, 30), (630, 30))
    baixo = pygame.draw.line(variaveis.tela, (0, 0, 0), (10, 450), (630, 450))
    esquerda = pygame.draw.line(variaveis.tela, (0, 0, 0), (10, 30), (10, 450))
    direita = pygame.draw.line(variaveis.tela, (0, 0, 0), (630, 30), (630, 450))
    centrocima = pygame.draw.line(variaveis.tela, (0, 0, 0), (320, 30), (320, 200))
    centrobaixo = pygame.draw.line(variaveis.tela, (0, 0, 0), (320, 240), (320, 450))
    if cobra.colliderect(cima) or cobra.colliderect(baixo) or cobra.colliderect(esquerda) or cobra.colliderect(direita)\
            or cobra.colliderect(centrobaixo) or cobra.colliderect(centrocima):
        morte()
