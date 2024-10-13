# assets.py
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('assets/images/bg.jpg')
    assets['bullet_sound'] = pygame.mixer.Sound('assets/music/effects/bullet.wav')
    assets['hit_sound'] = pygame.mixer.Sound('assets/music/effects/hit.wav')
    pygame.mixer.music.load('assets/music/sound/music.mp3')
    return assets
