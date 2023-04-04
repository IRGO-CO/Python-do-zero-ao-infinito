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
