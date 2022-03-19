import pygame.font
from gun import Gun
from pygame.sprite import Group
class Scores():
    '''Вывод счета'''
    def __init__(self, screen, stats):
        "Инициализуем подсчет очков"
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (189,189,189)
        self.font = pygame.font.SysFont(None,36)
        self.image_score()
        self.image_high_score()
        self.image_lifes()

    def image_score(self):
        """Преобразовывет текст в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 5
        self.score_rect.top = 5
    def image_high_score(self):
        "Рекорд"
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0,0,0) )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 5

    def image_lifes(self):
        "Колличество жизней"
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 545 + gun_number * gun.rect.width
            gun.rect.y = 5
            self.guns.add(gun)
    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)



