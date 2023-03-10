import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()

    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))

    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    dicionario_de_arquivos['font_coracao'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    dicionario_de_arquivos['cereja'] = pygame.image.load(os.path.join(IMG_DIR, 'cherries.png')).convert()
    pygame.Surface.set_colorkey(dicionario_de_arquivos['cereja'], [255, 255, 255])

    dicionario_de_arquivos['flor'] = pygame.image.load(os.path.join(IMG_DIR, 'flower.png')).convert()
    pygame.Surface.set_colorkey(dicionario_de_arquivos['flor'], [255, 255, 255])

    dicionario_de_arquivos['arvore-fruta'] = pygame.image.load(os.path.join(IMG_DIR, 'fruit-tree.png')).convert()
    pygame.Surface.set_colorkey(dicionario_de_arquivos['arvore-fruta'], [255, 255, 255])

    dicionario_de_arquivos['joaninha'] = pygame.image.load(os.path.join(IMG_DIR, 'ladybug.png')).convert()
    pygame.Surface.set_colorkey(dicionario_de_arquivos['joaninha'], [255, 255, 255])

    dicionario_de_arquivos['arvore'] = pygame.image.load(os.path.join(IMG_DIR, 'tree.png')).convert()
    pygame.Surface.set_colorkey(dicionario_de_arquivos['arvore'], [255, 255, 255])

    dicionario_de_arquivos['input'] = pygame.image.load(os.path.join(IMG_DIR, 'input.png')).convert_alpha()
    dicionario_de_arquivos['input'] = pygame.transform.scale(dicionario_de_arquivos['input'], (400, 100))

    # Carrega os sons do jogo
    dicionario_de_arquivos['success_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'success.wav'))
    dicionario_de_arquivos['fail_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'wah-wah.wav'))
    return dicionario_de_arquivos
