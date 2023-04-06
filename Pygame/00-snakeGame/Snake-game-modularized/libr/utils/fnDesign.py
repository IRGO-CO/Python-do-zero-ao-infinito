from . import *


def pontuacao():
    pygame.draw.rect(variaveis.tela, (255, 0, 0), (530, 3, 101, 23))
    fontePontos = pygame.font.SysFont('comic sans', 15)
    txtPontos = f'Pontos: {variaveis.pontos:^3}'
    txtformatPontos = fontePontos.render(txtPontos, True, (255, 255, 255))
    variaveis.tela.blit(txtformatPontos, (540, 3))


def mostraFase():
    if variaveis.pontos >= 0:
        variaveis.fase = 1
    else:
        if variaveis.pontos >= 100:
            variaveis.fase = 2
        if variaveis.pontos >= 200:
            variaveis.fase = 3
    pygame.draw.rect(variaveis.tela, (255, 0, 0), (467, 3, 60, 23))
    fonteFase = pygame.font.SysFont('comic sans', 15)
    txtFase = f'Fase: {variaveis.fase}'
    txtformatFase = fonteFase.render(txtFase, True, (255, 255, 255))
    variaveis.tela.blit(txtformatFase, (472, 3))


def passaFase():
    fontep = pygame.font.SysFont('arial', 60)
    txtp = f'Fase {fase + 1}'
    txtformatp = fontep.render(txtp, True, (255, 255, 255))
    rettxtp = txtformatp.get_rect()
    rettxtp.center = (largura // 2, altura // 2)
    cont = 0
    while True:
        tela.fill((200, 0, 0))
        pygame.mixer.music.stop()
        for c in pygame.event.get():
            if c.type == QUIT:
                pygame.quit()
                exit()
        if cont > 3000:
            return
        tela.blit(txtformatp, rettxtp)
        cont += 1
        pygame.display.update()
