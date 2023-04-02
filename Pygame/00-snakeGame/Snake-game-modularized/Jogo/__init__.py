import lib

import pygame

while True:
    lib.variaveis.relogio.tick(lib.variaveis.frame)
    lib.variaveis.tela.fill((255, 255, 255))

    cobra = pygame.draw.rect(lib.variaveis.tela, (200, 0, 0), (lib.variaveis.cobrax, lib.variaveis.cobray, 10, 10))
    comida = pygame.draw.circle(lib.variaveis.tela, (255, 0, 0), (lib.variaveis.comidax, lib.variaveis.comiday), 5)

    lib.variaveis.cobrax += lib.variaveis.direcaox * lib.variaveis.velocidade
    lib.variaveis.cobray += lib.variaveis.direcaoy * lib.variaveis.velocidade
    lib.corpo()
    if cobra.colliderect(comida):
        lib.comer()
    lib.controle()
    if lib.variaveis.cobrax < 0:
        lib.variaveis.cobrax = 640
    if lib.variaveis.cobrax > 640:
        lib.variaveis.cobrax = 0
    if lib.variaveis.cobray < 0:
        lib.variaveis.cobray = 480
    if lib.variaveis.cobray > 480:
        lib.variaveis.cobray = 0
    pygame.display.update()
