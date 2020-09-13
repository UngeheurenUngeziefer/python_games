import pyxel
from random import randint
from music import Music
from creatures import Creatures
from updaters import Updater
from player import Player

class SquareRun():
    '''Запускает игру'''
    def __init__(self):
        self.start_game = 0                     # начальный экран
        self.score = 0                          # счёт игрока
        self.highscore = 0                      # рекорд
        self.WIDTH = 160                        # ширина окна
        self.HEIGHT = 120                       # высота окна
        
        pyxel.init(self.WIDTH, self.HEIGHT, caption="Square Run")    # размер окна, название окна
        pyxel.image(0).load(0, 0, "../pics/logo.png")     # путь к лого
        pyxel.run(self.update, self.draw)                            # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):             # выход из игры по Q
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_TAB):         # переход на следующий экран по TAB
            self.start_game = 1                 # переход на экран игры
            Music().game_music()
            Music().tab_button_pressed()
            if self.highscore < self.score:     # логика рекорда
                self.highscore = self.score
            elif self.highscore >= self.score:
                pass
            self.score = 0                  # обнуление счёта
        elif self.start_game == 1:          # если игра запущена то запускаем функцию игрока, врагов и друзей
            Player().update_player()
            Updater().enemy_counter()
            Updater().square_counter()

    def draw(self):
        if self.start_game == 0:                                                     # ЭКРАН Начало игры
            pyxel.cls(0)                                                             # фон с аргументом чёрный
            pyxel.text(56, self.HEIGHT // 3, "Welcome to", pyxel.frame_count % 16)   # мигающий текст с координатами
            pyxel.text(37, self.HEIGHT - self.HEIGHT // 3, "Press TAB to start!", pyxel.frame_count % 16)
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)                                       # параметры лого
        elif self.start_game == 2:                                                   # ЭКРАН Конец игры
            Player().player_outside()
            pyxel.cls(0)
            if self.score > self.highscore:
                pyxel.text(46, 31, f"New Best: {self.score}!", pyxel.frame_count % 16)
            else:
                pyxel.text(46, 31, f"Highscore: {self.highscore}", pyxel.frame_count % 16)
                pyxel.text(46, 41, f"Your score: {self.score}", pyxel.frame_count % 16)
            pyxel.text(58, 21, "GAME OVER!", pyxel.frame_count % 16)
            pyxel.text(37, 81, "Press TAB to Restart!", pyxel.frame_count % 16)
            pyxel.text(45, 91, "Press Q to Quit!", pyxel.frame_count % 16)
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)
        elif self.start_game == 1:                                                   # ЭКРАН Игра
            pyxel.cls(13)
            pyxel.load("../square_run_assets.pyxres")                                   # загружаем скины
            Creatures().clouds_draw()
            Creatures().enemy_draw()
            Creatures().square_draw()
            Player().draw_player()
            s = "SCORE {:>4}".format(self.score)                                     # формат отображения счёта
            pyxel.text(5, 4, s, 1)
            pyxel.text(4, 4, s, 7)

SquareRun()
