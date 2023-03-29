# Importa os pacotes e biblioteca
import pygame

from random import randint

from pygame.locals import *

from sys import exit

# Inicia o pygame
pygame.init()

# Fonte dos textos
fonte = pygame.font.SysFont('comic sans', 20, True, False)

# Define o tamanho da tela
altura = int(480)
largura = int(640)

# Gera a comida aleatoriamente
comiday = randint(35, 445)
comidax = randint(15, 625)
bonusx, bonusy = randint(15, 625), randint(35, 445)

# Define a posição velocidade e direção da cabeça da cobra
x = largura // 2
y = altura // 2
veloObj = 0
direObj = [1, 0]
sentido = 'direita'

# Cria a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Primeiro Jogo!')

# Define o 'frame rate'
relogio = pygame.time.Clock()

# Cria uma lista para a cabeça e o corpo da cobra
cabeca = list()
liscobra = list()
corpo = ''

# Contadores
cont = 0
pontos = 0
totPontos = pontos
volume = 0.4
frame = 0
# Define o som de colisão
colisao = pygame.mixer.Sound('ES_Suction Pop 6 - SFX Producer.wav')

# Loop principal do jogo
while True:

    # Pausa a música enquanto o jogo esta parado
    if veloObj == 0:
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load('HoliznaCC0 - Adventure Begins Loop.mp3')
        pygame.mixer.music.play(-1)

    # Aumenta e pausa a cobra
    relogio.tick(frame)

    # Preenche a tela com a cor branca
    tela.fill((255, 255, 255))

    # Formata os pontos
    mensagem = f'Pontos: {pontos}'
    msgformt = fonte.render(mensagem, True, (0, 0, 0))

    # Condição de encerramento do pygame e feichar a janela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # DESENHA OS OBJETOS NA TELA
    # Pontos
    pygame.draw.rect(tela, (255, 0, 0), (500, 0, 150, 30))
    tela.blit(msgformt, (509, 0))
    # Cobra, comida e bonus
    cobra = pygame.draw.rect(tela, (200, 0, 0), (x, y, 10, 10))
    comida = pygame.draw.circle(tela, (210, 0, 0), [comidax, comiday], 5)
    if pontos % 10 == 0 and pontos != 0:
        bonus = pygame.draw.circle(tela, (210, 0, 0), (bonusx, bonusy), 8)

        # Faz a cobra 'comer' o bonus
        if cobra.colliderect(bonus):
            colisao.play()
            bonusx = randint(15, 625)
            bonusy = randint(35, 445)
            pontos += 2
            totPontos = pontos
            veloObj += 0.002
            colisao.play()

    # Movimenta a cobra automaticamente
    x += direObj[0] * veloObj
    y += direObj[1] * veloObj

    # Pausa e Inicia o jogo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_ESCAPE]:
        veloObj = totpontos = 0
    if veloObj == 0:
        msg = [f'Pressione ENTER', f'Pressione "M" para silenciar a música']
        msgF = [fonte.render(msg[0], True, (0, 0, 0)), fonte.render(msg[1], True, (0, 0, 0))]
        tela.blit(msgF[0], (largura // 2 - 80, altura // 2 - 25))
        if teclas[pygame.K_RETURN]:
            if pontos == 0:
                liscobra.clear()
                comiday = randint(35, 445)
                comidax = randint(15, 625)
                x, y = largura // 2, altura // 2
            veloObj = 1.0 + (pontos * 0.001)

    # Controla a cobra
    elif sentido != 'baixo' and teclas[pygame.K_w] or sentido != 'baixo' and teclas[pygame.K_UP]:
        if not teclas[pygame.K_d] and not teclas[pygame.K_a]:
            sentido = 'cima'
            direObj[1] = -1
            direObj[0] = 0
    elif sentido != 'cima' and teclas[pygame.K_s] or sentido != 'cima' and teclas[pygame.K_DOWN]:
        if not teclas[pygame.K_d] and not teclas[pygame.K_a]:
            sentido = 'baixo'
            direObj[1] = 1
            direObj[0] = 0
    elif sentido != 'esquerda' and teclas[pygame.K_d] or sentido != 'esquerda' and teclas[pygame.K_RIGHT]:
        sentido = 'direita'
        direObj[0] = 1
        direObj[1] = 0
    elif sentido != 'direita' and teclas[pygame.K_a] or sentido != 'direita' and teclas[pygame.K_LEFT]:
        sentido = 'esquerda'
        direObj[0] = -1
        direObj[1] = 0

    # Aumenta a velocidade da cobra
    if teclas[pygame.K_SPACE]:
        frame = 200
    else:
        frame = 120

    # Limita a tela
    if cobra.colliderect(pygame.draw.line(tela, (0, 0, 0), (10, 30), (630, 30))):
        pontos = veloObj = 0
    if cobra.colliderect(pygame.draw.line(tela, (0, 0, 0), (10, 450), (630, 450))):
        pontos = veloObj = 0
    if cobra.colliderect(pygame.draw.line(tela, (0, 0, 0), (10, 30), (10, 450))):
        pontos = veloObj = 0
    if cobra.colliderect(pygame.draw.line(tela, (0, 0, 0), (630, 30), (630, 450))):
        pontos = veloObj = 0

    # Exibe o total de pontos e 'game over'
    if veloObj == 0 and totPontos != 0 and pontos == 0:
        msgg = [f'{str(totPontos)} Pontos!!!', 'GAME OVER']
        msggg = [fonte.render(msgg[0], True, (0, 0, 0)), fonte.render(msgg[1], True, (0, 0, 0))]
        if len(liscobra) != 0:
            tela.blit(msggg[0], (largura / 2 - 45, altura / 2 - 50))
            tela.blit(msggg[1], (largura / 2 - 60, altura / 3))

    # Faz a cobra comer a comida
    if cobra.colliderect(comida):
        colisao.play()
        comiday = randint(35, 445)
        comidax = randint(15, 625)
        pontos += 1
        totPontos = pontos
        veloObj += 0.001

    # Aumenta a cobra
    cabeca = ([int(x), int(y)])
    if cabeca not in liscobra and pontos != 0:
        if cont == 10:
            liscobra.insert(0, cabeca)
            cont = 0
            del (liscobra[pontos:])
        cont += 1
    for c, i in enumerate(liscobra):
        if pontos != 0 or veloObj == 0:
            corpo = pygame.draw.rect(tela, (200, 0, 0), (i[0], i[1], 10, 10))

        # Verifica se a cabeça da cobra colidiu com o corpo
        if corpo.colliderect(cobra) and c > 5:
            pontos = veloObj = 0

        # Verifica se a comida e o bonus vai nascer 'em baixo' da cobra
        if corpo.colliderect(comida):
            comidax = randint(35, 445)
            comiday = randint(15, 625)

    # Atualiza a tela no final de cada loop
    pygame.display.update()
