import pyxel
from random import randint

# класс игры
class SquareRun:
    def __init__(self):
        self.start_game = 0                     # начальный экран
        self.score = 0                          # счёт игрока
        self.highscore = 0                      # рекорд
        self.player_x = 30                      # расположение игрока по х
        self.player_y = 100                     # расположение игрока по у
        self.WIDTH = 160                        # ширина окна
        self.HEIGHT = 120                       # высота окна
        self.clouds = [(10, 25), (70, 35), (120, 15)]
        self.enemy = [(i * 80, randint(8, 104), True) for i in range(3)]                    # 3 аргумента
        self.square = [(i * 60, randint(0, 104), randint(0, 4), True) for i in range(4)]    # 4 аргумента
        pyxel.init(self.WIDTH, self.HEIGHT, caption="Square Run")    # размер окна, название окна
        pyxel.image(0).load(0, 0, "../Square_Run/pics/logo.png")     # путь к лого
        pyxel.run(self.update, self.draw)                            # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):             # выход из игры по Q
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_TAB):         # переход на следующий экран по TAB
            self.start_game = 1                 # переход на экран игры
            pyxel.play(1, 7, loop=True)         # музыка во время игры 1 канал
            pyxel.play(2, 5)                    # звук при нажатии на TAB
            if self.highscore < self.score:     # логика рекорда
                self.highscore = self.score
            elif self.highscore >= self.score:
                pass
            self.score = 0                  # обнуление счёта
        elif self.start_game == 1:          # если игра запущена то запускаем функцию игрока, врагов и друзей
            self.update_player()
            for i, v in enumerate(self.enemy):
                self.enemy[i] = self.update_enemy(*v)
            for i, v in enumerate(self.square):
                self.square[i] = self.update_square(*v)

    def draw(self):
        if self.start_game == 0:                                                     # ЭКРАН Начало игры
            pyxel.cls(0)                                                             # фон с аргументом чёрный
            pyxel.text(56, self.HEIGHT // 3, "Welcome to", pyxel.frame_count % 16)   # мигающий текст с координатами
            pyxel.text(37, self.HEIGHT - self.HEIGHT // 3, "Press TAB to start!", pyxel.frame_count % 16)
            pyxel.blt(58, 55, 0, 0, 0, 38, 16)                                       # параметры лого
        elif self.start_game == 2:                                                   # ЭКРАН Конец игры
            self.player_x = -10                                          # прячем гг за экран чтобы не набирались очки
            self.player_y = -10
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
            pyxel.load("square_run_assets.pyxres")                                   # загружаем скины
            offset = (pyxel.frame_count // 8) % 160
            for i in range(2):
                for x, y in self.clouds:
                    pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)
                    pyxel.blt(x + i * 160 - offset, y + 20, 0, 0, 32, 56, 8, 12)
            offset = pyxel.frame_count % 160                                         # движущийся фон низ
            for i in range(2):
                pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 13)             # рисуем гг
            s = "SCORE {:>4}".format(self.score)                                     # формат отображения счёта
            pyxel.text(5, 4, s, 1)
            pyxel.text(4, 4, s, 7)
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
            self.player_y = min(self.player_y + 5, self.HEIGHT - 16)
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, self.WIDTH - 16)
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 0)

    def update_enemy(self, x, y, is_active):
        # Столкновение с игроком
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            pyxel.play(2, 4)                                # звук при умирании во 2 канал
            pyxel.play(1, 2)                                # музыка при умирании в 1 канал
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
            pyxel.play(2, 4)                                 # звук при столкновении с другом во 2 канал
        x -= 2
        if x < -40:
            x += 240
            y = randint(0, 104)
            kind = randint(0, 2)
            is_active = True
        return x, y, kind, is_active

SquareRun()
