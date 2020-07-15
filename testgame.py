import pygame
from pygame.locals import *
import cardfunctions

pygame.init()

class Card(pygame.sprite.Sprite):
    def __init__(self, cardID, flipped):
        super().__init__()
        self.image = pygame.image.load("images/card-back.png")
        self.surf = pygame.Surface()

window = pygame.display.set_mode((300, 300))