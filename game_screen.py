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

    item_sort = 'cereja'

    cont = True
    ultima = pygame.time.get_ticks()
    texto = ''
    qnt = 1
    erro = 0
    pontuacao = 0
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
            qnt+=1
        if cont == False and now - ultima > 3000:
            cont = True
            ultima = now
            lista_imagens = pygame.sprite.Group()
            lista = ['cereja','flor','arvore-fruta','joaninha','arvore']
            sort = random.sample(lista,k=qnt)
            for j in sort:
                item_sort = random.choice(sort)
                quantos = (random.randint(5,10))
                for i in range(quantos):
                    print(quantos)
                    item = Item(dicionario_de_arquivos,j)
                    lista_imagens.add(item)
            
            
            if erro >= 3:
                DONE
            
            
            if str(quantos) == texto:
                pontuacao += 1
                dicionario_de_arquivos['success_sound'].play()
                print("acertou")
                
            else:
                erro += 1 
                dicionario_de_arquivos['fail_sound'].play()
                print("errou")   
                      

            
            
        
        


        # ----- Trata eventos
        
        for event in pygame.event.get():
            # ----- Verifica consequências
            print(event)
            
            if event.type == pygame.KEYDOWN:
                
                texto +=  event.unicode 
                

            if event.type == pygame.QUIT:
                state = DONE
            
        

            
            

        
        # ----- Gera saídas
        window.fill(WHITE)  # Preenche com a cor branca
        if cont == True:
            lista_imagens.draw(window)
            texto = ''
        else:
            window.blit(dicionario_de_arquivos["input"], (200, 275))
            text = dicionario_de_arquivos['font'].render(texto,True,BLACK)
            teste= text.get_rect()
            teste.x = 400
            teste.y = 320
            window.blit(text,teste)

            txt= dicionario_de_arquivos['font'].render("Quantos",True,BLACK)
            window.blit(pygame.transform.scale(dicionario_de_arquivos[item_sort],(40,45)),(505,225))
            test= text.get_rect()
            test.x = 330
            test.y = 245
            window.blit(txt,test)




            

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
