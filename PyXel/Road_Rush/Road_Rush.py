import pyxel
from time import sleep
from random import randint

class RoadRush:
    def __init__(self):
        self.start_game = 0  # начальный экран
        self.road_x1 = 43
        self.road_x2 = 103
        self.enemy_speed = 6
        self.counter = -1
        self.counts_list = [3, 2, 1, 'GO!']
        self.gameover = 0

        self.score = 0
        self.player_x = 80
        self.player_y = 130
        self.width, self.height = 160, 160
        pyxel.init(self.width, self.height, caption="Road Rush")    # размер окна, название окна
        pyxel.image(1).load(0, 0, "./pics/logo.png")                # 1 - лого, 0 - редактор, 2 - бэк
        self.enemy = [(i * 80, 400, True) for i in range(1)]                    # 3 аргумента
        pyxel.run(self.update, self.draw)                           # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):                                 # выход из игры по Q
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_R):
            self.start_game = 2
        elif pyxel.btnp(pyxel.KEY_TAB):
            self.start_game = 1
        elif self.start_game == 2:
            self.update_player()
            for i, v in enumerate(self.enemy):
                self.enemy[i] = self.update_enemy(*v)

    def draw(self):
        # ЭКРАН Стартовый
        if self.start_game == 0:
            pyxel.text(58, 50, "Welcome to", pyxel.frame_count % 16)  # мигающий текст с координатами
            pyxel.blt(30, 60, 1, 0, 0, 100, 50)
            pyxel.text(56, 120, "TAB to start", pyxel.frame_count % 16)
            pyxel.text(62, 130, "Q to quit", pyxel.frame_count % 16)

        # ЭКРАН 1 УРОВЕНЬ
            # Отсчёт 3, 2, 1, GO!
        elif self.start_game == 1:
            pyxel.load("./road_rush_assets.pyxres")  # загружаем скины
            pyxel.image(2).load(0, 0, "./pics/Road_Rush_Map_0.png")  # путь к бэку 1 уровня
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)               # бэк
            pyxel.blt(73, 1, 0, 41, 1, 42, 160, 13)                         # разметка
            pyxel.blt(43, 100, 0, 100, 0, 60, 160, 13)                      # разметка START
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)     # гг
            self.counter += 1       # счётчик для отсчёта
            pyxel.text(self.width // 2, self.height // 2, str(self.counts_list[self.counter]), col=7)   # текст отсчёта
            self.update_score()     # счёт
            sleep(1)                # пауза
            if self.counter < 3:
                pyxel.play(0, 0)    # звук на 3 2 1 - 0 канал
            else:
                pyxel.play(0, 1)    # звук на GO!   - 0 канал
                self.start_game = 2     # переход в игру

        # ИГРА
        elif self.start_game == 2:


            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)            # бэк
            pyxel.blt(73, 1, 0, 41, 1, 42, 160, 13)                      # разметка
            pyxel.blt(43, 100, 0, 100, 0, 60, 160, 13)                   # разметка START
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            for x, y, is_active in self.enemy:                                       # рисуем врагов
                pyxel.blt(x, -y, 0, 8, 0, 8, 16, 13)
            self.update_score()

        elif self.start_game == 10:
            pyxel.cls(0)
            pyxel.text(58, 21, "GAME OVER!", pyxel.frame_count % 16)
            pyxel.text(37, 81, "Press R to Restart!", pyxel.frame_count % 16)
            pyxel.text(45, 91, "Press Q to Quit!", pyxel.frame_count % 16)
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)

    def update_enemy(self, x, y, is_active):
        # Столкновение с игроком
        if is_active and abs(x - self.player_x) < 18 and abs(y - (-self.player_y)) < 18:
            self.counter = -1
            self.start_game = 10
            y = 200



        y -= self.enemy_speed                       # скорость полёта врагов (шаг по х)
        if y < -200:                  # враги пропадают за экраном в минусе по х и появляются справа за экраном
            y += 240
            x = randint(43, 103 - 8)

        return x, y, is_active

    def update_score(self):
        s = "SCORE {:>4}".format(self.score)  # формат отображения счёта
        pyxel.text(125, 4, s, 1)
        pyxel.text(125, 4, s, 7)

    def update_player(self):
        # назначаем управление на кнопки, ограничиваем передвижение экраном
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, self.width - 57 - 8)
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 43)
        #if pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.KEY_UP):

RoadRush()
