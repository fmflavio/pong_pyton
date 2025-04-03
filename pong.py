import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Definindo as dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong")

# Definindo a fonte
fonte = pygame.font.SysFont("arial", 30)

# Função para desenhar a tela
def desenhar_tela(paddle1, paddle2, bola, pontuacao1, pontuacao2):
    tela.fill(PRETO)
    
    # Desenha as raquetes
    pygame.draw.rect(tela, BRANCO, paddle1)
    pygame.draw.rect(tela, BRANCO, paddle2)
    
    # Desenha a bola
    pygame.draw.ellipse(tela, BRANCO, bola)
    
    # Desenha o placar
    texto = fonte.render(f"{pontuacao1} - {pontuacao2}", True, BRANCO)
    tela.blit(texto, (LARGURA_TELA // 2 - texto.get_width() // 2, 20))
    
    # Atualiza a tela
    pygame.display.update()

# Função principal do jogo
def jogar():
    # Inicializa as variáveis do jogo
    paddle1 = pygame.Rect(30, ALTURA_TELA // 2 - 60, 20, 120)  # Raquete do jogador 1
    paddle2 = pygame.Rect(LARGURA_TELA - 50, ALTURA_TELA // 2 - 60, 20, 120)  # Raquete do jogador 2
    bola = pygame.Rect(LARGURA_TELA // 2 - 15, ALTURA_TELA // 2 - 15, 30, 30)  # Bola

    velocidade_bola_x = 5 * random.choice((1, -1))
    velocidade_bola_y = 5 * random.choice((1, -1))
    velocidade_raquete = 7

    pontuacao1 = 0
    pontuacao2 = 0

    relogio = pygame.time.Clock()
    rodando = True
    
    while rodando:
        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        # Movimento das raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= velocidade_raquete
        if teclas[pygame.K_s] and paddle1.bottom < ALTURA_TELA:
            paddle1.y += velocidade_raquete
        if teclas[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= velocidade_raquete
        if teclas[pygame.K_DOWN] and paddle2.bottom < ALTURA_TELA:
            paddle2.y += velocidade_raquete

        # Movimento da bola
        bola.x += velocidade_bola_x
        bola.y += velocidade_bola_y

        # Colisão da bola com o topo e fundo
        if bola.top <= 0 or bola.bottom >= ALTURA_TELA:
            velocidade_bola_y *= -1

        # Colisão da bola com as raquetes
        if bola.colliderect(paddle1) or bola.colliderect(paddle2):
            velocidade_bola_x *= -1
        
        # Pontuação
        if bola.left <= 0:
            pontuacao2 += 1
            bola = pygame.Rect(LARGURA_TELA // 2 - 15, ALTURA_TELA // 2 - 15, 30, 30)
            velocidade_bola_x *= random.choice((1, -1))
            velocidade_bola_y *= random.choice((1, -1))
        
        if bola.right >= LARGURA_TELA:
            pontuacao1 += 1
            bola = pygame.Rect(LARGURA_TELA // 2 - 15, ALTURA_TELA // 2 - 15, 30, 30)
            velocidade_bola_x *= random.choice((1, -1))
            velocidade_bola_y *= random.choice((1, -1))

        # Atualiza a tela
        desenhar_tela(paddle1, paddle2, bola, pontuacao1, pontuacao2)
        
        # Controla a taxa de atualização do jogo
        relogio.tick(60)

    # Salva a pontuação no arquivo de texto
    with open("pontuacoes.txt", "a") as f:
        f.write(f"Pontuação final: Jogador 1: {pontuacao1} - Jogador 2: {pontuacao2}\n")

    pygame.quit()

# Inicia o jogo
jogar()
