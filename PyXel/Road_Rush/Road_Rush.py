import pyxel
from time import sleep

class RoadRush:
    def __init__(self):
        self.start_game = 0  # начальный экран
        self.counter = 0
        self.score = 0
        self.player_x = 80
        self.player_y = 130
        self.WIDTH, self.HEIGHT = 160, 160
        pyxel.init(self.WIDTH, self.HEIGHT, caption="Road Rush")    # размер окна, название окна
        pyxel.image(0).load(0, 0, "./pics/logo.png")                # путь к лого

        pyxel.run(self.update, self.draw)                           # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):                                 # выход из игры по Q
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_TAB):
            self.start_game = 1
            pyxel.load("./road_rush_assets.pyxres")  # загружаем скины
            pyxel.image(1).load(0, 0, "./pics/Road_Rush_Map_0.png")  # путь к бэку 1 уровня
        elif self.start_game == 2:
            self.update_player()

    def draw(self):
        if self.start_game == 0:                                            # ЭКРАН Стартовый
            pyxel.text(58, 50, "Welcome to", pyxel.frame_count % 16)  # мигающий текст с координатами
            pyxel.blt(30, 60, 0, 0, 0, 100, 50)
            pyxel.text(56, 120, "TAB to start", pyxel.frame_count % 16)
            pyxel.text(62, 130, "Q to quit", pyxel.frame_count % 16)
        if self.start_game == 1:                 # ЭКРАН 1 УРОВЕНЬ
            if self.counter == 0:               # Отсчёт 3, 2, 1, GO!
                pyxel.blt(0, 0, 1, 0, 0, self.WIDTH, self.HEIGHT)
                pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)
                pyxel.text(self.WIDTH // 2, self.HEIGHT // 2, str(3), pyxel.frame_count % 16)
                self.update_score()
                pyxel.play(0, 0)
                sleep(1)
                self.counter += 1
            elif self.counter == 1:
                pyxel.blt(0, 0, 1, 0, 0, self.WIDTH, self.HEIGHT)
                pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)
                pyxel.text(self.WIDTH // 2, self.HEIGHT // 2, str(3), pyxel.frame_count % 16)
                self.update_score()
                pyxel.play(0, 0)
                sleep(1)
                self.counter += 1
                self.counter += 1
            elif self.counter == 2:
                pyxel.blt(0, 0, 1, 0, 0, self.WIDTH, self.HEIGHT)
                pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)
                pyxel.text(self.WIDTH // 2, self.HEIGHT // 2, str(3), pyxel.frame_count % 16)
                self.update_score()
                pyxel.play(0, 0)
                sleep(1)
                self.counter += 1
                self.counter += 1
            elif self.counter == 3:
                pyxel.blt(0, 0, 1, 0, 0, self.WIDTH, self.HEIGHT)
                pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)
                pyxel.text(self.WIDTH // 2, self.HEIGHT // 2, str(3), pyxel.frame_count % 16)
                self.update_score()
                pyxel.play(0, 0)
                sleep(1)
                self.counter += 1
            else:
                self.start_game = 2
                self.update_score()

        # Игра
        elif self.start_game == 2:
            self.counter += 1
            pyxel.blt(0, 0, 1, 0, 0, self.WIDTH, self.HEIGHT)
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)  # рисуем гг
            self.update_score()

    def count_func(self):
        counts_list = [3, 2, 1, 'GO!']
        pyxel.blt(0, 0, 1, 0, 0, self.WIDTH, self.HEIGHT)
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 16, 13)
        pyxel.text(self.WIDTH // 2, self.HEIGHT // 2, str(counts_list[self.counter]), pyxel.frame_count % 16)
        self.update_score()
        if self.counter < 3:
            pyxel.play(0, 0)
            sleep(1)
        elif self.counter == 3:
            pyxel.play(0, 1)
            sleep(1)




    def update_score(self):
        s = "SCORE {:>4}".format(self.score)  # формат отображения счёта
        pyxel.text(125, 4, s, 1)
        pyxel.text(125, 4, s, 7)

    def update_player(self):
        # назначаем управление на кнопки, ограничиваем передвижение экраном
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, self.WIDTH - 57 - 8)
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 43)




RoadRush()
