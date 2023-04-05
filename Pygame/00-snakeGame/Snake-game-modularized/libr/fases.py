import pygame

from . import *


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


def fase2():
    pygame.draw.line(variaveis.tela, (0, 0, 0), (10, 30), (630, 30))
    pygame.draw.line(variaveis.tela, (0, 0, 0), (10, 450), (630, 450))
    pygame.draw.line(variaveis.tela, (0, 0, 0), (10, 30), (10, 450))
    pygame.draw.line(variaveis.tela, (0, 0, 0), (630, 30), (630, 450))
