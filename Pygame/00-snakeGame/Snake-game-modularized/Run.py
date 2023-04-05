import libr
import pygame

while True:

    libr.utils.variaveis.relogio.tick(libr.utils.variaveis.frame)
    libr.utils.variaveis.tela.fill((255, 255, 255))
    libr.fase1()

    cobra = pygame.draw.circle(libr.utils.variaveis.tela, (200, 0, 0), (
        libr.utils.variaveis.cobrax, libr.utils.variaveis.cobray), 5)
    comida = pygame.draw.circle(libr.utils.variaveis.tela, (255, 0, 0), (
        libr.utils.variaveis.comidax, libr.utils.variaveis.comiday), 5)

    libr.utils.variaveis.cobrax += libr.utils.variaveis.direcaox * libr.utils.variaveis.velocidade
    libr.utils.variaveis.cobray += libr.utils.variaveis.direcaoy * libr.utils.variaveis.velocidade
    libr.corpo()
    if cobra.colliderect(comida):
        libr.comer()
    libr.controle()

    pygame.display.update()
