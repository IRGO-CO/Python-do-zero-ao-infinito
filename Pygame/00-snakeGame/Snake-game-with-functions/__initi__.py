# Importa os pacotes e biblioteca
import pygame

from random import randint

import pygame.mixer
from pygame.locals import *

from sys import exit


def aumentar(lista):
    global comprimento
    lista_cobra.append([cobrax, cobray])
    for i in lista:
        pygame.draw.rect(tela, (255, 0, 0), (i[0], i[1], 10, 10))


def resetar():
    global pontos, comprimento, comidax, comiday, cobrax, cobray
    pontos = 0
    comprimento = 5
    cobrax = largura // 2
    cobray = altura // 2
    comidax = randint(15, 625)
    comiday = randint(35, 445)
    jogo()


def morte():
    while True:
        pygame.mixer.music.stop()
        tela.fill((200, 0, 0))
        for c in pygame.event.get():
            if c.type == QUIT:
                pygame.quit()
                exit()
            if c.type == KEYDOWN:
                if c.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if c.key == K_RETURN or c.key == K_KP_ENTER:
                    pygame.mixer.music.play(-1)
                    lista_cobra.clear()
                    resetar()
        tela.blit(txtformat0, rettxt0)
        tela.blit(txtformat1, rettxt1)
        pygame.display.update()


def comer():
    global comidax, comiday, pontos, comprimento, corrandom, velocidade
    colisao.play()
    corrandom = [randint(0, 255), randint(0, 255), randint(0, 255)]
    comidax = randint(15, 625)
    comiday = randint(35, 445)
    pontos += 1
    comprimento += 2
    velocidade += 0.01


def menu():
    fontem = pygame.font.SysFont('arial', 45, True, True)
    txtm = 'Pressione ENTER para jogar'
    txtformatm = fontem.render(txtm, True, (255, 255, 255))
    rettxtm = txtformatm.get_rect()
    rettxtm.center = (largura // 2, altura // 2)

    while True:
        pygame.mixer.music.stop()
        tela.fill((200, 0, 0))
        for c in pygame.event.get():
            if c.type == QUIT:
                pygame.quit()
                exit()
            if c.type == KEYDOWN:
                if c.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if c.key == K_RETURN or c.key == K_KP_ENTER:
                    pygame.mixer.music.play(-1)
                    jogo()
        tela.blit(txtformatm, rettxtm)
        pygame.display.update()


def jogo():
    global pontos, comprimento, cobrax, cobray, comidax, comiday, velocidade, controley, controlex, frame
    while True:
        relogio.tick(frame)
        tela.fill((corrandom[0], corrandom[1], corrandom[2]))

        # Formata os pontos
        mensagem = f'Pontos: {pontos}'
        msgformt = fontep.render(mensagem, True, (0, 0, 0))

        # DESENHA OS OBJETOS NA TELA
        # Pontos
        pygame.draw.rect(tela, (255, 0, 0), (500, 0, 150, 30))
        tela.blit(msgformt, (509, 0))
        # Cobra, comida
        cobra = pygame.draw.rect(tela, (200, 0, 0), (cobrax, cobray, 10, 10))
        comida = pygame.draw.circle(tela, (210, 0, 0), (comidax, comiday), 5)

        # Condição de encerramento do pygame e feichar a janela
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # Contola o jogo
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    if controley == velocidade:
                        pass
                    else:
                        controlex = 0
                        controley = -velocidade
                elif event.key == K_DOWN or event.key == K_s:
                    if controley == -velocidade:
                        pass
                    else:
                        controlex = 0
                        controley = velocidade
                elif event.key == K_LEFT or event.key == K_a:
                    if controlex == velocidade:
                        pass
                    else:
                        controlex = -velocidade
                        controley = 0
                elif event.key == K_RIGHT or event.key == K_d:
                    if controlex == -velocidade:
                        pass
                    else:
                        controlex = velocidade
                        controley = 0
        cobrax += controlex
        cobray += controley
        # Aumenta a velocidade da cobra
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            frame = 120
        else:
            frame = 60

        # Faz a cobra comer a comida
        if cobra.colliderect(comida):
            comer()
        aumentar(lista_cobra)

        # Limita a tela
        if cobrax > 640:
            morte()
        if cobrax < 0:
            morte()
        if cobray > 480:
            morte()
        if cobray < 0:
            morte()
        # Faz a cobra colidir com o proprio corpo
        if lista_cobra.count([cobrax, cobray]) > 1:
            morte()

        if comprimento < len(lista_cobra):
            del lista_cobra[0]

        # Atualiza a tela no final de cada loop
        pygame.display.update()


# Inicia o pygame
pygame.init()

# Define o tamanho da tela
largura = int(640)
altura = int(480)

# Fonte dos textos
fontep = pygame.font.SysFont('comic sans', 20, True, False)
fonte0 = pygame.font.SysFont('arial', 100, True, True)
fonte1 = pygame.font.SysFont('arial', 15, True, True)
txt = ['Game Over!', 'Pressione ENTER para jogar novamente ou ESC para sair']
txtformat0 = fonte0.render(txt[0], True, (255, 255, 255))
txtformat1 = fonte1.render(txt[1], True, (255, 255, 255))
rettxt0 = txtformat0.get_rect()
rettxt1 = txtformat1.get_rect()
rettxt0.center = (largura // 2, altura // 2.5)
rettxt1.center = (largura // 2, altura // 2)

# Cria a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

# Define o 'frame rate'
relogio = pygame.time.Clock()

# Contadores
corrandom = [255, 255, 255]
volume = 0.4
pontos = 0
cobrax = largura // 2
cobray = altura // 2
comidax = randint(15, 625)
comiday = randint(35, 445)
velocidade: int = 3
controlex = velocidade
controley = 0
comprimento = int(5)
frame = 60

# Define o som
colisao = pygame.mixer.Sound('ES_Suction Pop 6 - SFX Producer.wav')
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.load('HoliznaCC0 - Adventure Begins Loop.mp3')
pygame.mixer.music.play(-1)

lista_cabeca = list()
lista_cobra = list()

menu()
