import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK, WHITE
from assets import carrega_arquivos
from sprites import Item

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()
    lista_imagens = pygame.sprite.Group()
    item = Item(dicionario_de_arquivos,"cereja")
    lista_imagens.add(item)

    
    for i in range(random.randint(5,10)):
        item = Item(dicionario_de_arquivos,"cereja")
        lista_imagens.add(item)



# ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int(pygame.time.get_ticks() - last_update)
        print(segundos)
        if segundos > 5000:
            lista_imagens.empty()
            window.fill(WHITE)
            pygame.display.update()
            pygame.time.wait(3000)
            for i in range(random.randint(5,10)):
                item = Item(dicionario_de_arquivos,"cereja")
                lista_imagens.add(item)
            last_update = pygame.time.get_ticks()
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(WHITE)  # Preenche com a cor branca
        lista_imagens.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
