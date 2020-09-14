import pyxel
from random import randint
from music import Music
from background import Background
from text import Text
from constants import WIDTH, HEIGHT

class Game:
    def __init__(self):
        self.start_game = 0                     # начальный экран
        self.score = 0                          # счёт игрока
        self.highscore = 0                      # рекорд
        self.player_x = 30                      # расположение игрока по х
        self.player_y = 100                     # расположение игрока по у
        self.enemy = [(i * 80, randint(8, 104), True) for i in range(3)]                    # 3 аргумента
        self.square = [(i * 60, randint(0, 104), randint(0, 4), True) for i in range(4)]    # 4 аргумента
        pyxel.init(WIDTH, HEIGHT, caption="Square Run")    # размер окна, название окна
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
            self.score = 0
        elif self.start_game == 1:          # если игра запущена то запускаем функцию игрока, врагов и друзей
            self.update_player()
            for i, v in enumerate(self.enemy):
                self.enemy[i] = self.update_enemy(*v)
            for i, v in enumerate(self.square):
                self.square[i] = self.update_square(*v)

    def draw(self):
        if self.start_game == 0:                                                     # ЭКРАН Начало игры
            Background().color('black')                                                        # фон с аргументом чёрный
            Text().start_text()
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)                                       # параметры лого
        elif self.start_game == 2:                                                   # ЭКРАН Конец игры
            self.player_x = -10                                          # прячем гг за экран чтобы не набирались очки
            self.player_y = -10
            Background().color('black')
            if self.score > self.highscore:
                Text().new_best(self.score)
            else:
                Text().highscore_text(self.score, self.highscore)
            Text().final_text()
        elif self.start_game == 1:                                                   # ЭКРАН Игра
            Background().color('grey')
            pyxel.load("square_run_assets.pyxres")                                   # загружаем скины
            Background().clouds_draw()
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 13)             # рисуем гг
            Text().score_view(self.score)
            for x, y, is_active in self.enemy:                                       # рисуем врагов
                pyxel.blt(x, y, 0, 0, 16, 24, 8, 13)
            for x, y, kind, is_active in self.square:                                # рисуем друзей
                if is_active:
                    pyxel.blt(x, y, 0, 16 + kind * 16, 0, 16, 16, 13)

    def update_player(self):
        # назначаем управление на кнопки, ограничиваем передвижение экраном
        if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
            self.player_y = max(self.player_y - 5, 0)
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            self.player_y = min(self.player_y + 5, HEIGHT - 16)
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, WIDTH - 16)
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 0)

    def update_enemy(self, x, y, is_active):
        # Столкновение с игроком
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            Music().death_music()
            self.start_game = 2                             # Игра окончена
        x -= 4                       # скорость полёта врагов (шаг по х)
        if x < -40:                  # враги пропадают за экраном в минусе по х и появляются справа за экраном
            x += 240
            y = randint(8, 104)
        return x, y, is_active

    def update_square(self, x, y, kind, is_active):
        # если мы сталкиваемся с другом
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            is_active = False
            self.score += (kind + 1) * 100                   # +100 очков за квадрат, +200 за прямоуг., +300 за треуг.
            Music().friend_eat_music()
        x -= 2
        if x < -40:
            x += 240
            y = randint(0, 104)
            kind = randint(0, 2)
            is_active = True
        return x, y, kind, is_active
Game()
