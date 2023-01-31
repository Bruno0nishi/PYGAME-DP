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

  

    cont = True
    ultima = pygame.time.get_ticks()
    
# ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int(pygame.time.get_ticks() - last_update)
        #print(segundos)
        now = pygame.time.get_ticks()
        #Renderize o texto digitado pelo jogador sobre o input
        if cont == True and now - ultima > 5000:
            cont = False
            ultima = now
        if cont == False and now - ultima > 3000:
            cont = True
            ultima = now
            lista_imagens = pygame.sprite.Group()
            for i in range(random.randint(5,10)):
                item = Item(dicionario_de_arquivos,"cereja")
                lista_imagens.add(item)
            
            
        
        


        # ----- Trata eventos
        
        for event in pygame.event.get():
            # ----- Verifica consequências
            print(event)
            """texto = ""
            
            if event.type == pygame.KEYDOWN:
                
                event.unicode += texto 
                font = pygame.font.SysFont(None,48)
                texto1 = font.render(texto, True, BLACK)
                window.blit(texto1, (250, 275))
                """

            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(WHITE)  # Preenche com a cor branca
        if cont == True:
            lista_imagens.draw(window)
        else:
            window.blit(dicionario_de_arquivos["input"], (200, 275))
            text = dicionario_de_arquivos['font'].render(event.unicode,True,BLACK)
            teste= text.get_rect()
            teste.x = 400
            teste.y = 320
            window.blit(text,teste)
            

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
