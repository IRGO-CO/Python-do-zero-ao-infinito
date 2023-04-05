import pygame

from random import randint

comidax = randint(13, 627)
comiday = randint(13, 467)
velocidade = 0.5

cobrax = 640 // 2
cobray = 480 // 2
direcaox = 1
direcaoy = 0

listaCorpo = list()
cabeça = list()
tamanho = 5
pontos = 0

pygame.init()
largura = 640
altura = 480
relogio = pygame.time.Clock()
frame: int = 60

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game - Saga')
