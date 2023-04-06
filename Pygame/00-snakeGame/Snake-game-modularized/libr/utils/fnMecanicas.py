from . import variaveis

from libr.menu import *

import pygame

import pygame.key

from random import randint

from pygame.locals import *

from libr.utils.sons import *

from sys import exit


def comer():
    comeu.play()
    variaveis.comidax = randint(18, 625)
    variaveis.comiday = randint(38, 444)
    variaveis.velocidade += 0.001
    variaveis.tamanho += 2
    variaveis.pontos += 1


def controle():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                if variaveis.direcaoy == 1:
                    pass
                else:
                    variaveis.direcaox = 0
                    variaveis.direcaoy = -1
            if event.key == K_s or event.key == K_DOWN:
                if variaveis.direcaoy == -1:
                    pass
                else:
                    variaveis.direcaox = 0
                    variaveis.direcaoy = 1
            if event.key == K_a or event.key == K_LEFT:
                if variaveis.direcaox == 1:
                    pass
                else:
                    variaveis.direcaox = -1
                    variaveis.direcaoy = 0
            if event.key == K_d or event.key == K_RIGHT:
                if variaveis.direcaox == -1:
                    pass
                else:
                    variaveis.direcaox = 1
                    variaveis.direcaoy = 0
            if event.key == K_ESCAPE:
                menu_pause()

        espaco = pygame.key.get_pressed()
        if espaco[pygame.K_SPACE]:
            variaveis.velocidade = 3 + (variaveis.pontos * 0.001)
        else:
            variaveis.velocidade = 2 + (variaveis.pontos * 0.001)


def corpo():
    variaveis.listaCorpo.insert(0, [variaveis.cobrax, variaveis.cobray])
    if len(variaveis.listaCorpo) > variaveis.tamanho - 4:
        del variaveis.listaCorpo[variaveis.tamanho:]
    for i in variaveis.listaCorpo:
        pygame.draw.circle(variaveis.tela, (200, 0, 0), (i[0], i[1]), 5)
    if variaveis.listaCorpo.count([variaveis.cobrax, variaveis.cobray]) > 1:
        morte()


def resetar():
    variaveis.cobrax = 640 // 2
    variaveis.cobray = 480 // 2
    variaveis.tamanho = 5
    variaveis.pontos = 0


def morte():
    menu_morte()
    resetar()
