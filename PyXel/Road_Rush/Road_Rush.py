import pyxel
from time import sleep
from random import randint

class RoadRush:
    def __init__(self):
        self.width, self.height = 160, 160  # ширина, высота окна
        self.start_game = 0                     # начальный экран
        self.road_x1 = 43                       # начало дороги по х
        self.road_x2 = 103                      # конец дороги по х
        self.road_size = range(self.road_x1, self.road_x2 - 8)
        self.enemy_speed = 6                    # скорость вражеской машины
        self.counter = -1                      # счётчик для отсчёта 3, 2, 1
        self.counts_list = [3, 2, 1, 'GO!']     # список отсчёт
        self.clock = 0                          # часы
        self.score = 0                          # счёт
        self.highscore = 0                      # рекорд
        self.player_x = 80                      # координата х игрока
        self.player_y = 130                     # координата у игрока
        self.progress_y = 129                   # ползунок прогресса
        self.road_markdown = 1                  # положение разметки
        self.road_start = 120                   # положение линии старта
        self.road_finish = 0                    # положение линии финиша
        self.cars_number = 1                    # количество машин
        self.side_sprites_y = -60                 # положение боковых домов
        self.lvl = 1
        self.enemy = [(i * 9, randint(300, self.enemy_speed * 150), True) for i in range(self.cars_number)]
        pyxel.init(self.width, self.height, caption="Road Rush")         # размер окна, название окна
        pyxel.image(0).load(0, 0, "./pics/logo.png")                     # лого
        pyxel.run(self.update, self.draw)       # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):                                 # выход из игры по Q
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_R):                               # рестарт на R
            self.restart_all_nums()
        elif pyxel.btnp(pyxel.KEY_TAB):                             # начало игры по TAB
            self.start_game = 1
            self.update_highscore()
        elif self.start_game == 2:                                  # прошёл отсчёт
            self.player_controls()                                  # подключаем управление
            for i, v in enumerate(self.enemy):                      # генерируем случайные авто противника
                self.enemy[i] = self.update_enemy(*v)
            self.road_markdown_moving()                             # движение разметки
            self.road_start_md_moving()                             # движение линии старта
        elif self.start_game == 3:
            pyxel.play(3, 5)
        elif self.start_game == 6:
            self.player_controls()
            for i, v in enumerate(self.enemy):
                self.enemy[i] = self.update_enemy(*v)
            self.road_markdown_moving()
            self.road_start_md_moving()
        elif self.start_game == 9:
            self.player_controls()
            for i, v in enumerate(self.enemy):
                self.enemy[i] = self.update_enemy(*v)
            self.road_markdown_moving()
            self.road_start_md_moving()

    def draw(self):
        # ЭКРАН Стартовый
        if self.start_game == 0:
            pyxel.cls(0)
            pyxel.text(58, 50, "Welcome to", pyxel.frame_count % 16)    # мигающий текст с координатами
            pyxel.blt(30, 60, 0, 0, 0, 100, 50)
            pyxel.text(56, 120, "TAB to start", pyxel.frame_count % 16)
            pyxel.text(62, 130, "Q to quit", pyxel.frame_count % 16)

        # Отсчёт 3, 2, 1, GO!
        elif self.start_game == 1:
            pyxel.load("./road_rush_assets.pyxres")                         # загружаем скины из tilemap
            pyxel.image(2).load(0, 0, "./pics/3.png")         # путь к бэку 1 уровня
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)               # back
            pyxel.blt(43, self.road_start, 0, 0, 82, 60, 90, 13)            # линия старта
            pyxel.blt(20, self.side_sprites_y, 1, 0, 0, 100, 160, 13)       # боковые дома кусты
            pyxel.blt(39, -30, 0, 91, 0, 94, 199, 13)                       # разметка и поребрик
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)     # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)              # ползунок прогресса
            self.counter += 1                                               # счётчик
            pyxel.text(self.width // 2, self.height // 2,
                       str(self.counts_list[self.counter]), col=7)          # текст отсчёта
            self.show_score_highscore()                                     # показать счёт
            sleep(1)                                                        # пауза 1 сек
            if self.counter < 3:                                            # если (счётчик == 3)
                pyxel.play(1, 0)                                            # звук на 3 2 1 - 0 канал
            if self.counter == 3:
                pyxel.play(1, 1)
                self.start_game = 2                                         # переход в игру

        # 1 УРОВЕНЬ
        elif self.start_game == 2:
            self.lvl = 1
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)             # фон
            self.side_sprites()                                           # боковые спрайты
            pyxel.blt(39, self.road_markdown, 0, 91, 0, 94, 199, 13)      # разметка и поребрик
            pyxel.blt(43, self.road_start, 0, 0, 82, 60, 90, 13)          # линия старта
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)   # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)            # ползунок прогресса
            self.clock += 1                                               # счётчик часы

            if self.clock % 50 == 0:        # если число делится на 50 без остатка то
                self.progress_y -= 4        # поднимаем ползунок прогресса на 4 вверх
            elif self.progress_y == 9:
                self.clock = 0
                self.start_game = 3         # переходим на экран финиша

            for x, y, is_active in self.enemy:                  # рисуем врагов
                if x in self.road_size:                         # ограничение дорогой
                    pyxel.blt(x, -y, 0, 8, 0, 8, 16, 13)

                if self.clock > 500:                            # 2 машины
                    self.cars_number = 2
                    self.plus_one_car(x, y)

                if self.clock > 1000:                           # 3 машины
                    self.cars_number = 3
                    self.plus_one_car(x + 16, y + 32)

                if self.clock > 1200:                           # 4 машины
                    self.cars_number = 4
                    self.plus_one_car(x - 16, y - 60)

                else:
                    pass
            self.show_score_highscore()     # показываем счёт
#####################################################################
        # ФИНИШ
        elif self.start_game == 3:
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)  # фон
            if self.road_finish < self.player_y:  # пока линия финиша не достигнет игрока
                pyxel.blt(43, self.road_finish, 0, 0, 82, 60, 90, 13)  # рисуем линию финиша
                self.road_finish += self.enemy_speed  # опускаем её со скоростью соперников
                self.side_sprites()  # отрисовка боковых спрайтов
                self.road_markdown += 4  # скорость разметки
                pyxel.blt(39, self.road_markdown, 0, 91, 0, 94, 199, 13)  # разметка и поребрик
                pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # рисуем игрока
                pyxel.blt(6, self.progress_y, 0, 0, 30, 8, 37, 13)  # ползунок прогресса
                self.show_score_highscore()  # показываем счёт
            else:
                pyxel.cls(0)

                pyxel.text(60, 50,  # пишем ФИНИШ
                           'FINISH!', col=7)
                pyxel.text(40, 60, "Your Score is {:>1}".format(self.score), pyxel.frame_count % 16)
                self.clock += 1
                if self.clock > 100 and self.lvl == 1:
                    self.start_game = 4
                    self.clock = 0
                elif self.clock > 100 and self.lvl == 2:
                    self.start_game = 7
                    self.clock = 0

#####################################################################
        # ЭКРАН 2 уровень
        elif self.start_game == 4:
            pyxel.cls(0)
            pyxel.text(58, 50, "Level 2", pyxel.frame_count % 16)
            sleep(2)
            self.lvl = 2
            self.restart_nums_second_lvl()
            self.start_game = 5

        # Отсчёт 3, 2, 1
        elif self.start_game == 5:
            pyxel.load("./road_rush_assets.pyxres")  # загружаем скины из tilemap
            pyxel.image(2).load(0, 0, "./pics/4.png")  # путь к бэку 2 уровня
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)  # back
            pyxel.blt(43, self.road_start, 0, 0, 82, 60, 90, 13)  # линия старта
            pyxel.blt(20, self.side_sprites_y, 1, 148, 0, 248, 160, 13)  # боковые спрайты
            pyxel.blt(39, -30, 0, 91, 0, 94, 199, 13)  # разметка и поребрик
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)  # ползунок прогресса
            self.counter += 1  # счётчик
            pyxel.text(self.width // 2, self.height // 2,
                       str(self.counts_list[self.counter]), col=7)  # текст отсчёта
            self.show_score_highscore()  # показать счёт
            sleep(1)  # пауза 1 сек
            if self.counter < 3:  # если (счётчик == 3) то другой звук
                pyxel.play(0, 0)  # звук на 3 2 1 - 0 канал
            else:
                pyxel.play(0, 1)  # звук на GO!   - 0 канал
                self.enemy = [(i * 9, self.enemy_speed * 350, True) for i in range(self.cars_number)]
                self.start_game = 6  # переход в игру

        # 2 УРОВЕНЬ
        elif self.start_game == 6:
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей
            pyxel.blt(0, 0, 2, 0, 0, self.width, self.height)  # фон
            self.side_sprites()  # боковые спрайты
            pyxel.blt(39, self.road_markdown, 0, 91, 0, 94, 199, 13)  # разметка и поребрик
            pyxel.blt(43, self.road_start, 0, 0, 82, 60, 90, 13)  # линия старта
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)  # ползунок прогресса
            self.clock += 1  # счётчик часы

            if self.clock % 50 == 0:  # если число делится на 50 без остатка то
                self.progress_y -= 4  # поднимаем ползунок прогресса на 4 вверх
            elif self.progress_y == 9:
                self.clock = 0
                self.start_game = 3  # переходим на экран финиша

            for x, y, is_active in self.enemy:  # рисуем врагов
                if x in self.road_size:  # ограничение дорогой
                    pyxel.blt(x, -y, 0, 16, 0, 24, 16, 13)

                if self.clock > 500:  # 2 машины
                    self.cars_number = 2
                    self.plus_one_car(x, y)

                else:
                    pass

            self.show_score_highscore()  # показываем счёт

            # ФИНИШ

#####################################################################
        # ЭКРАН 3 уровень
        elif self.start_game == 7:
            pyxel.cls(0)
            pyxel.text(58, 50, "Level 3", pyxel.frame_count % 16)
            sleep(2)
            self.lvl = 3
            self.restart_nums_third_lvl()
            self.start_game = 8

        # Отсчёт 3, 2, 1
        elif self.start_game == 8:
            pyxel.load("./road_rush_assets2.pyxres")  # загружаем скины из tilemap
            self.lvl = 3
            # х игры, у игры, файл, х в файле, у в файле, x2 в файле, у2 в файле, колкей

            pyxel.blt(0, 0, 1, 0, 0, self.width, self.height)  # back
            pyxel.blt(43, self.road_start, 0, 0, 82, 60, 90, 13)  # линия старта

            pyxel.blt(20, self.side_sprites_y, 2, 0, 0, 100, 248, 13)  # боковые спрайты

            pyxel.blt(39, -30, 0, 86, 0, 141, 215, 13)  # разметка

            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)  # ползунок прогресса

            self.counter += 1  # счётчик
            pyxel.text(self.width // 2, self.height // 2,
                       str(self.counts_list[self.counter]), col=7)  # текст отсчёта
            self.show_score_highscore()  # показать счёт
            sleep(1)  # пауза 1 сек
            if self.counter < 3:  # если (счётчик == 3) то другой звук
                pyxel.play(0, 0)  # звук на 3 2 1 - 0 канал
            else:
                pyxel.play(0, 1)  # звук на GO!   - 0 канал
                self.enemy = [(i * 9, self.enemy_speed * 350, True) for i in range(self.cars_number)]
                self.start_game = 9  # переход в игру

        # 3 УРОВЕНЬ
        elif self.start_game == 9:
            pyxel.blt(0, 0, 1, 0, 0, self.width, self.height)  # back
            self.side_sprites()  # боковые спрайты
            pyxel.blt(39, -30, 0, 86, 0, 141, 215, 13)  # разметка
            pyxel.blt(43, self.road_start, 0, 0, 82, 60, 90, 13)  # линия старта
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # гг
            pyxel.blt(6, self.progress_y, 0, 0, 17, 7, 23, 13)  # ползунок прогресса
            self.clock += 1  # счётчик часы

            if self.clock % 50 == 0:  # если число делится на 50 без остатка то
                self.progress_y -= 4  # поднимаем ползунок прогресса на 4 вверх
            elif self.progress_y == 9:
                self.clock = 0
                pyxel.play(2, 3)
                self.start_game = 11

            for x, y, is_active in self.enemy:  # рисуем врагов
                if x in self.road_size:  # ограничение дорогой
                    pyxel.blt(x, -y, 0, 24, 0, 40, 32, 13)

                if self.clock > 500:  # 2 машины
                    self.cars_number = 2
                    self.plus_one_car(x, y)

                if self.clock > 1000:  # 3 машины
                    self.cars_number = 3
                    self.plus_one_car(x + 16, y + 32)

                if self.clock > 1200:  # 4 машины
                    self.cars_number = 4
                    self.plus_one_car(x - 16, y - 60)

                else:
                    pass

            self.show_score_highscore()  # показываем счёт

        # ПРОИГРЫШ
        elif self.start_game == 10:
            pyxel.cls(0)                                                        # фон чёрный
            pyxel.text(58, 21, "GAME OVER!", pyxel.frame_count % 16)
            pyxel.text(37, 81, "Press R to Restart!", pyxel.frame_count % 16)
            pyxel.text(45, 91, "Press Q to Quit!", pyxel.frame_count % 16)
            pyxel.text(43, 101, "Your Score is {:>1}".format(self.score), pyxel.frame_count % 16)
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)                                  # часть моделей
            self.clock = 0

        # КОНЕЦ ИГРЫ
        elif self.start_game == 11:
            pyxel.cls(0)  # фон чёрный
            pyxel.image(0).load(0, 0, "./pics/logo.png")
            pyxel.blt(30, 60, 0, 0, 0, 100, 50)                         # лого
            pyxel.text(43, 41, "CONGRATULATIONS!", pyxel.frame_count % 16)
            pyxel.text(45, 121, "Press Q to Quit!", pyxel.frame_count % 16)
            pyxel.text(43, 131, "Your Score is {:>1}".format(self.score), pyxel.frame_count % 16)



    def update_enemy(self, x, y, is_active):
        # Столкновение с игроком, х и у соперников отличаются меньше чем размер корпуса авто гг
        if self.lvl < 3:
            pyxel.play(2, 3)
        else:
            pyxel.play(1, 2)

        if self.lvl < 3 and is_active and abs(x - self.player_x) < 8 and abs(y - (-self.player_y)) < 16:
            self.counter = -1         # счётчик обнуляется
            self.start_game = 10      # сценарий проигрыш
            y = 800                   # авто соперника улетает вверх за экран
            pyxel.play(0, 4)
        elif self.lvl == 3 and is_active and abs(x - self.player_x) < 16 and abs(y - (-self.player_y)) < 32:
            self.counter = -1  # счётчик обнуляется
            self.start_game = 10  # сценарий проигрыш
            y = 800  # авто соперника улетает вверх за экран
            pyxel.play(0, 4)

        y -= self.enemy_speed         # скорость полёта врагов (шаг по у)

        if self.lvl == 2 and -70 < y < 0 and x < self.player_x:
            x += 2
        if self.lvl == 2 and -70 < y < 0 and x > self.player_x:
            x -= 2

        if y < -300:                  # если авто внизу за экраном
            y += 300                  # то телепортируем его наверх
            if self.lvl < 3:
                x = randint(self.road_x1, self.road_x2 - 8)  # ограничение дорогой (минус ширина корпуса авто)
            else:
                x = randint(self.road_x1, self.road_x2 - 32)
            self.score += self.cars_number * 100         # +100 очков за каждое обогнанное авто

        return x, y, is_active

    def road_start_md_moving(self):
        if self.road_start >= 120:          # функция приводящая разметку СТАРТ в движение
            self.road_start += 0.5
        elif self.road_start > 200:
            pass

    def road_markdown_moving(self):
        # функция приводящая разметку в движение, картинка дёргается вверх вниз на 4 пикселя
        if self.road_markdown == 1:
            self.road_markdown -= 4
        else:
            self.road_markdown += 4

    def restart_nums_second_lvl(self):
        self.enemy_speed = 6  # функция обнуляющая все показатели на значение по умолчанию
        self.clock = 0
        self.counter = -1
        self.progress_y = 129
        self.road_markdown = 1
        self.road_start = 120
        self.cars_number = 1
        self.side_sprites_y = -90

    def restart_nums_third_lvl(self):
        self.restart_nums_second_lvl()
        self.road_x1 = 43
        self.road_x2 = 93


    def restart_all_nums(self):
        self.enemy_speed = 6        # функция обнуляющая все показатели на значение по умолчанию
        self.clock = 0
        self.counter = -1
        self.road_start = 130
        self.start_game = 1
        self.update_highscore()
        self.player_x = 80
        self.player_y = 130
        self.progress_y = 129
        self.road_markdown = 1
        self.road_start = 120
        self.cars_number = 1
        self.side_sprites_y = -60

    def side_sprites(self):
        # движение боковых спрайтов, картинка накладывается сама на себя сверху и пропадает снизу
        if self.lvl == 1:
            if self.side_sprites_y < 160:
                self.side_sprites_y += self.enemy_speed
                pyxel.blt(20, self.side_sprites_y, 1, 0, 0, 100, 160, 13)
                pyxel.blt(20, self.side_sprites_y - 170, 1, 0, 0, 100, 160, 13)
            elif self.side_sprites_y > 160:
                self.side_sprites_y = 0
                pyxel.blt(20, self.side_sprites_y, 1, 0, 0, 100, 160, 13)
                pyxel.blt(20, self.side_sprites_y - 170, 1, 0, 0, 100, 160, 13)
        if self.lvl == 2:
            if self.side_sprites_y < 160:
                self.side_sprites_y += self.enemy_speed
                pyxel.blt(20, self.side_sprites_y, 1, 148, 0, 248, 160, 13)
                pyxel.blt(20, self.side_sprites_y - 170, 1, 148, 0, 248, 160, 13)
            elif self.side_sprites_y > 160:
                self.side_sprites_y = 0
                pyxel.blt(20, self.side_sprites_y, 1, 148, 0, 248, 160, 13)
                pyxel.blt(20, self.side_sprites_y - 170, 1, 148, 0, 248, 160, 13)
        if self.lvl == 3:
            if self.side_sprites_y < 160:
                self.side_sprites_y += self.enemy_speed
                pyxel.blt(20, self.side_sprites_y, 2, 0, 0, 100, 248, 13)
                pyxel.blt(20, self.side_sprites_y - 170, 2, 0, 0, 100, 248, 13)
            elif self.side_sprites_y > 160:
                self.side_sprites_y = 0
                pyxel.blt(20, self.side_sprites_y, 2, 0, 0, 100, 248, 13)
                pyxel.blt(20, self.side_sprites_y - 170, 2, 0, 0, 100, 248, 13)



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

    def plus_one_car(self, x, y):
        if x in self.road_size:
            if self.lvl == 1:
                #     < 10
                if x < self.road_x1 + 10:
                    pyxel.blt(x + 40, -(y + 90), 0, 8, 0, 8, 16, 13)
                #      10 < x < 20
                elif self.road_x1 + 10 <= x < self.road_x2 - 40:
                    pyxel.blt(x + 10, -(y + 30), 0, 8, 0, 8, 16, 13)
                #      20 < x < 30
                elif self.road_x1 + 20 <= x < self.road_x2 - 30:
                    pyxel.blt(x + 23, -(y + 100), 0, 8, 0, 8, 16, 13)
                #      30 < x < 40
                elif self.road_x1 + 30 <= x < self.road_x2 - 20:
                    pyxel.blt(x - 25, -(y + 47), 0, 8, 0, 8, 16, 13)
                #      40 < x < 50
                elif self.road_x1 + 40 <= x < self.road_x2 - 10:
                    pyxel.blt(x - 32, -(y + 52), 0, 8, 0, 8, 16, 13)
                #      x > 50
                elif x >= self.road_x2 - 10:
                    pyxel.blt(x - 47, -(y + 35), 0, 8, 0, 8, 16, 13)

            if self.lvl == 2:
                if x < self.road_x1 + 10:
                    pyxel.blt(x + 40, -(y + 90), 0, 16, 0, 24, 16, 13)
                elif self.road_x1 + 10 <= x < self.road_x2 - 40:
                    pyxel.blt(x + 10, -(y + 30), 0, 16, 0, 24, 16, 13)
                elif self.road_x1 + 20 <= x < self.road_x2 - 30:
                    pyxel.blt(x + 23, -(y + 100), 0, 16, 0, 24, 16, 13)
                elif self.road_x1 + 30 <= x < self.road_x2 - 20:
                    pyxel.blt(x - 25, -(y + 47), 0, 16, 0, 24, 16, 13)
                elif self.road_x1 + 40 <= x < self.road_x2 - 10:
                    pyxel.blt(x - 32, -(y + 52), 0, 16, 0, 24, 16, 13)
                elif x >= self.road_x2 - 10:
                    pyxel.blt(x - 47, -(y + 35), 0, 16, 0, 24, 16, 13)

    def player_controls(self):
        # назначаем управление на кнопки, ограничиваем передвижение экраном
        if self.lvl != 3 and (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            self.player_x = min(self.player_x + 5, self.width - 57 - 8)
        if self.lvl != 3 and (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            self.player_x = max(self.player_x - 5, 43)
        if self.lvl == 3 and pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, self.width - 69 - 8)
        if self.lvl == 3 and pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 43)


RoadRush()
