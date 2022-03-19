import pygame

import control

from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 900))
    pygame.display.set_caption("Space Invaders")
    bg_color=(0,0,0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    control.create_aliens(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        control.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun_pos()
            control.update_screen(bg_color,screen,stats,sc,gun,inos,bullets)
            control.update_bullets(screen,stats,sc,inos,bullets)
            control.update_aliens_pos(stats, screen,sc, gun, inos, bullets)


run()
