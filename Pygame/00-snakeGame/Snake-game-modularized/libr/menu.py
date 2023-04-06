import libr
from .utils.variaveis import *

from sys import exit

from pygame.locals import *

import pygame.key


def menu_pause():
    fontep = pygame.font.SysFont('arial', 30)
    txtp = ['Pressione ENTER para retornar',
            'ou ESC para sair']
    txtformatp = [fontep.render(txtp[0], True, (255, 255, 255)),
                  fontep.render(txtp[1], True, (255, 255, 255))]
    rettxtp = txtformatp[0].get_rect()
    rettxtp.center = (largura // 2, altura // 2.5)

    rettxtp1 = txtformatp[1].get_rect()
    rettxtp1.center = (largura // 2, altura // 2)

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
                    # pygame.mixer.music.play(-1)
                    return
        tela.blit(txtformatp[0], rettxtp)
        tela.blit(txtformatp[1], rettxtp1)
        pygame.display.update()


def menu_inicio():
    fontei = pygame.font.SysFont('arial', 30)
    txti = ['SNAKE GAME SAGA',
            'Pressione ENTER para começar']
    txtformati = [fontei.render(txti[0], True, (255, 255, 255)),
                  fontei.render(txti[1], True, (255, 255, 255))]
    rettxti = txtformati[0].get_rect()
    rettxti.center = (largura // 2, altura // 2.5)
    rettxti1 = txtformati[1].get_rect()
    rettxti1.center = (largura // 2, altura // 2)
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
                    # pygame.mixer.music.play(-1)
                    libr.passaFase()
                    return
        tela.blit(txtformati[0], rettxti)
        tela.blit(txtformati[1], rettxti1)
        pygame.display.update()


def menu_morte():
    fontei = pygame.font.SysFont('arial', 30)
    txti = [f'Você Morreu com {libr.variaveis.pontos} Pontos',
            'Pressione ENTER para recomeçar', ]
    txtformati = [fontei.render(txti[0], True, (255, 255, 255)),
                  fontei.render(txti[1], True, (255, 255, 255))]
    rettxti = txtformati[0].get_rect()
    rettxti.center = (largura // 2, altura // 2.5)
    rettxti1 = txtformati[1].get_rect()
    rettxti1.center = (largura // 2, altura // 2)
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
                    # pygame.mixer.music.play(-1)
                    return
        tela.blit(txtformati[0], rettxti)
        tela.blit(txtformati[1], rettxti1)
        pygame.display.update()
