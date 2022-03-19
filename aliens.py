import pygame

class Ino(pygame.sprite.Sprite):
    """Пришелец"""
    def __init__(self,screen):
        """Задаем и инициализируем пришельца"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def drawa(self):
        """Вывод на экран прешельца"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Перемещение прешельцев"""
        self.y += 0.005
        self.rect.y = self.y