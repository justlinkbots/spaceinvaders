import pygame
import sys
from bullet import Bullet
from aliens import Ino
from tkinter import messagebox

import time

def events(screen, gun, bullets):
    '''Управление'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Движение вправо наж
            if event.key == pygame.K_d:
                gun.moveright = True
            elif event.key == pygame.K_a:
                gun.moveleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen,gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Движение вправо наж
            if event.key == pygame.K_d:
                gun.moveright = False
            elif event.key == pygame.K_a:
                gun.moveleft = False

def update_screen(bg_color,screen,stats,sc,gun,inos,bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.draw()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen,stats,sc,inos, bullets):
    """Обновлять поз пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score +=100 * len(inos)
            sc.image_score()
            check_high_score(stats, sc)
            sc.image_lifes()
    if len(inos) == 0:
        bullets.empty()
        create_aliens(screen, inos)

def gun_dest(stats,screen,sc,gun,inos,bullets):
    """Уничтожение"""
    if stats.guns_left > 0:
        stats.guns_left -=1
        sc.image_lifes()
        inos.empty()
        bullets.empty()
        create_aliens(screen, inos)
        gun.create_new_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        messagebox.showinfo('Space Invaders', 'Игра окончена!')
        sys.exit()


def update_aliens_pos(stats, screen,sc, gun, inos, bullets):
    """Обновление позиции прешельцев """
    inos.update()
    if pygame.sprite.spritecollideany(gun,inos):
        gun_dest(stats,screen,gun,sc,inos,bullets)
    inos_check_pass(stats, screen,sc, gun, inos, bullets)

def inos_check_pass(stats, screen, gun,sc, inos, bullets):
    """Проверка добрались до базы"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites ():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_dest(stats, screen, gun,sc, inos, bullets)
            break


def create_aliens(screen, inos):
    """Создание армии"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2* ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800-400 - 2* ino_height)/ino_height)
    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

def check_high_score(stats,sc):
    """Проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt','w') as f:
            f.write(str(stats.high_score))
