import pygame
from pygame.sprite import Sprite
class Gun(Sprite):
    def __init__(self,screen):
        """Инициализация"""
        super(Gun,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.centrer = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False

    def draw(self):
        """Отрисовка"""
        self.screen.blit(self.image, self.rect)
    def update_gun_pos(self):
        """Обновление позиции"""
        if self.moveright and self.rect.right < self.screen_rect.right-10:
            self.centrer += 0.5
        if self.moveleft and self.rect.left > 10:
            self.centrer -= 0.5
        self.rect.centerx = self.centrer

    def create_new_gun(self):
        """Новая пушка"""
        self.centrer = self.screen_rect.centerx