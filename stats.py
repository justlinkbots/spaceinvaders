import pygame

class Stats():
    "Отслкживание статисткик"
    def __init__(self):
        "Иниц статистику"
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt','r') as f:
            self.high_score = int(f.readline())
    def reset_stats(self):
        """Статистика измен во время игры"""
        self.guns_left = 3
        self.score = 0
