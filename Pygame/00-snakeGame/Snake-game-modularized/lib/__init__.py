from random import randint

import pygame
import pygame.key

from pygame.locals import *

from sys import exit

from lib import variaveis


def comer():
    comeu = pygame.mixer.Sound('../ES_Suction Pop 6 - SFX Producer.wav')
    comeu.play()
    variaveis.comidax = randint(3, 637)
    variaveis.comiday = randint(3, 477)
    variaveis.velocidade += 0.001
    variaveis.tamanho += 2
    variaveis.pontos += 1


def controle():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                if variaveis.direcaoy == 1:
                    pass
                else:
                    variaveis.direcaox = 0
                    variaveis.direcaoy = -1
            if event.key == K_s:
                if variaveis.direcaoy == -1:
                    pass
                else:
                    variaveis.direcaox = 0
                    variaveis.direcaoy = 1
            if event.key == K_a:
                if variaveis.direcaox == 1:
                    pass
                else:
                    variaveis.direcaox = -1
                    variaveis.direcaoy = 0
            if event.key == K_d:
                if variaveis.direcaox == -1:
                    pass
                else:
                    variaveis.direcaox = 1
                    variaveis.direcaoy = 0

        espaco = pygame.key.get_pressed()
        if espaco[pygame.K_SPACE]:
            variaveis.velocidade = 3 + (variaveis.pontos * 0.001)
        else:
            variaveis.velocidade = 2 + (variaveis.pontos * 0.001)


def corpo():
    variaveis.listaCorpo.insert(0, [variaveis.cobrax, variaveis.cobray])
    if len(variaveis.listaCorpo) > variaveis.tamanho:
        del variaveis.listaCorpo[variaveis.tamanho:]
    for i in variaveis.listaCorpo:
        pygame.draw.rect(variaveis.tela, (255, 0, 0), (i[0], i[1], 10, 10))
    if variaveis.listaCorpo.count([variaveis.cobrax, variaveis.cobray]) > 1:
        morte()


def morte():
    pygame.quit()
    exit()
