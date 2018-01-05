import pygame

class GUI:

    def __init__(self): 
        self.hero = Hero("My Name")

class Hero(pygame.sprite.Sprite):

    def __init__(self, name):
        self.name = name
        self.rect = pygame.Rect(0, 0, 50, 50)
