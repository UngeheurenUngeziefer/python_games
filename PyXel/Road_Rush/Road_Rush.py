import pyxel
from time import sleep
from random import randint

class RoadRush:
    def __init__(self):
        self.width, self.height = 160, 160  # ширина, высота окна
        self.start_game = 0                     # начальный экран
        self.road_x1 = 43                       # начало дороги по х
        self.road_x2 = 103                      # конец дороги по х
        self.enemy_speed = 6                    # скорость вражеской машины
        self.counter = -1                       # счётчик для отсчёта 3, 2, 1
        self.counts_list = [3, 2, 1, 'GO!']     # список отсчёт

        self.clock = 0
        self.score = 0                          # счёт
        self.highscore = 0                      # рекорд
        self.player_x = 80                      # координата х игрока
        self.player_y = 130                     # координата у игрока
        self.progress_y = 129
        self.road_markdown = 1
        self.road_start = 120
        self.cars_number = 2

        pyxel.init(self.width, self.height, caption="Road Rush")         # размер окна, название окна
        pyxel.image(1).load(0, 0, "./pics/logo.png")                     # пути 0 - tilemap, 1 - logo, 2 - back
        self.enemy = [(i * 80,
                       randint(self.enemy_speed * 150, 1000),
                       True) for i in range(self.cars_number)]           # х внутри дороги, y за экраном на расстоянии в зависимости от скорости, True
        pyxel.run(self.update, self.draw)                                # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):                                 # выход из игры по Q
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_R):                               # рестарт на R
            self.enemy_speed = 6
            self.clock = 0
            self.counter = -1
            self.road_start = 130
            self.start_game = 1
            self.update_highscore()
        elif pyxel.btnp(pyxel.KEY_TAB):                             # начало игры по TAB
            self.start_game = 1
            self.update_highscore()
        elif self.start_game == 2:                                  # прошёл отсчёт
            self.player_controls()                                  # подключаем управление
            for i, v in enumerate(self.enemy):                      # генерируем случайные авто противника
                self.enemy[i] = self.update_enemy(*v)
            self.road_markdown_moving()                             # движение разметки
            self.road_start_md_moving()

    def draw(self):
        # ЭКРАН Стартовый
        if self.start_game == 0:
            pyxel.cls(0)
            pyxel.text(58, 50, "Welcome to", pyxel.frame_count % 16)    # мигающий текст с координатами
            pyxel.blt(30, 60, 1, 0, 0, 100, 50)                         # лого
            pyxel.text(56, 120, "TAB to start", pyxel.frame_count % 16)
            pyxel.text(62, 130, "Q to quit", pyxel.frame_count % 16)

        # ЭКРАН 1 УРОВЕНЬ
        # Отсчёт 3, 2, 1, GO!
        elif self.start_game == 1:
            pyxel.load("./road_rush_assets.pyxres")                     # загружаем скины из tilemap
            pyxel.image(2).load(0, 0, "./pics/Road_Rush_Map_0.png")     # путь к бэку 1 уровня
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)               # back
            pyxel.blt(43, self.road_start, 0, 0, 42, 60, 52, 7)             # линия старта
            pyxel.blt(39, -30, 0, 91, 0, 94, 199, 13)                       # разметка и поребрик
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)     # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)              # ползунок прогресса
            self.counter += 1                                               # счётчик
            pyxel.text(self.width // 2, self.height // 2,
                       str(self.counts_list[self.counter]), col=7)          # текст отсчёта
            self.show_score_highscore()                                             # счёт
            sleep(1)                                                        # пауза 1 сек

            if self.counter < 3:                                            # если (счётчик == 3) то другой звук
                pyxel.play(0, 0)                                            # звук на 3 2 1 - 0 канал
            else:
                pyxel.play(0, 1)                                            # звук на GO!   - 0 канал
                self.start_game = 2                                         # переход в игру

        # ИГРА
        elif self.start_game == 2:
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)  # back
            pyxel.blt(39, self.road_markdown, 0, 91, 0, 94, 199, 13)  # разметка и поребрик
            pyxel.blt(43, self.road_start, 0, 0, 42, 60, 52, 7)            # линия старта
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)      # ползунок прогресса
            self.clock += 1                 # счётчик часы
            if self.clock % 50 == 0:        # если число делится на 50 без остатка то
                self.progress_y -= 4        # поднимаем ползунок прогресса на 4 вверх
            elif self.progress_y < 10:
                self.start_game = 3         # переходим на экран финиша
            # elif self.progress_y > 100:
            #     self.cars_number = 3

            for x, y, is_active in self.enemy:                           # рисуем врагов
                if x in range(self.road_x1, self.road_x2 - 8):  # ограничение дорогой (минус ширина корпуса авто)
                    pyxel.blt(x, -y, 0, 8, 0, 8, 16, 13)
                else:
                    pass
            self.show_score_highscore()


        # ФИНИШ
        elif self.start_game == 3:
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)  # back
            pyxel.text(self.width // 2, self.height // 2, 'FINISH!', col=7)
            pyxel.blt(73, self.road_markdown, 0, 41, 1, 42, 160, 13)        # разметка

            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            pyxel.blt(6, self.progress_y, 0, 0, 30, 8, 37, 13)  # прогресс
            self.show_score_highscore()

        # КОНЕЦ ИГРЫ
        elif self.start_game == 10:
            pyxel.cls(0)                                                        # фон чёрный
            pyxel.text(58, 21, "GAME OVER!", pyxel.frame_count % 16)
            pyxel.text(37, 81, "Press R to Restart!", pyxel.frame_count % 16)
            pyxel.text(45, 91, "Press Q to Quit!", pyxel.frame_count % 16)
            pyxel.text(43, 101, "Your Score is {:>1}".format(self.score), pyxel.frame_count % 16)
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)                                  # часть tilemap
            self.clock = 0

    def update_enemy(self, x, y, is_active):

        # Столкновение с игроком, х и у соперников отличаются меньше чем размер корпуса авто гг
        if is_active and abs(x - self.player_x) < 8 and abs(y - (-self.player_y)) < 16:
            self.counter = -1         # счётчик обнуляется
            self.start_game = 10      # сценарий конец игры
            y = 800                   # авто соперника улетает вверх за экран

        y -= self.enemy_speed         # скорость полёта врагов (шаг по у)
        if y < -200:                  # если авто внизу за экраном
            y += 240                  # то телепортируем его вверх за экран
            x = randint(self.road_x1, self.road_x2 - 8)  # ограничение дорогой (минус ширина корпуса авто)
            self.score += 100         # +100 очков за каждое обогнанное авто

        return x, y, is_active

    def road_start_md_moving(self):
        if self.road_start >= 120:          # функция приводящая разметку СТАРТ в движение
            self.road_start += 0.5
        elif self.road_start > 200:
            pass

    def road_markdown_moving(self):
        if self.road_markdown == 1:         # функция приводящая разметку в движение
            self.road_markdown -= 4
        else:
            self.road_markdown += 4

    def show_score_highscore(self):
        s = "{:>1}".format(self.score)      # функция отображения счёта и рекорда
        pyxel.text(129, 4, 'SCORE:', 7)
        pyxel.text(129, 14, s, 7)
        pyxel.text(130, 30, 'BEST:', 7)
        hs = "{:>1}".format(self.highscore)
        pyxel.text(129, 40, hs, 7)

    def update_highscore(self):
        if self.score > self.highscore:       # функция обновления рекорда
            self.highscore = self.score
        self.score = 0

    def player_controls(self):
        # назначаем управление на кнопки, ограничиваем передвижение экраном
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, self.width - 57 - 8)
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 43)
        # if pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.KEY_UP):

RoadRush()
