import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        """Пуля в позиции корабля"""
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 189,189,189
        self.speed = 2
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули"""
        self.y -= self.speed
        self.rect.y= self.y
    def draw_bullet(self):
        """Торисовка пули"""
        pygame.draw.rect(self.screen,self.color,self.rect)