import pyxel
from random import randint

class Game:
    def __init__(self):
        self.width, self.height = 100, 100
        self.player_x, self.player_y = 43, 83
        self.enemy = [(i * 8, randint(0, 300)) for i in range(10)]
        self.friend = [(i * 8, randint(0, 300)) for i in range(10)]
        self.score = 0
        self.highscore_file = open('score.txt', 'r').read()
        self.highscore = open('score.txt', 'r').read()
        self.is_alive = True
        self.lvl = 0

        self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 0, 0, 7, 7  # координаты модели гг

        pyxel.init(self.width, self.height, caption="Pyxel Rain")  # размер окна, название окна
        pyxel.run(self.update, self.draw)  # запуск программы

    def update(self):
        if pyxel.btnp(pyxel.KEY_TAB):
            self.lvl = 1
            pyxel.play(1, 2, loop=True)

        if self.score < 100 and self.lvl != 0:
            self.lvl = 1
        else:
            if str(self.score)[0] == '1':
                self.lvl = 2
            if str(self.score)[0] == '2':
                self.lvl = 3
            if str(self.score)[0] == '3':
                self.lvl = 4
            if str(self.score)[0] == '4':
                self.lvl = 5
            if str(self.score)[0] == '5':
                self.lvl = 6
            if str(self.score)[0] == '6':
                self.lvl = 7
            if str(self.score)[0] == '7':
                self.lvl = 8
            if str(self.score)[0] == '8':
                self.lvl = 9
            if str(self.score)[0] == '9':
                self.lvl = 10

        if self.lvl in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.player_controls()
            for i, v in enumerate(self.enemy):  # генерируем случайные авто противника
                self.enemy[i] = self.update_enemy(*v)
            for i, v in enumerate(self.friend):  # генерируем случайные авто противника
                self.friend[i] = self.update_friend(*v)

        if pyxel.btnp(pyxel.KEY_Q):  # выход из игры по Q
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):  # рестарт на R
            pyxel.play(1, 2, loop=True)
            self.lvl = 1
            self.is_alive = True
            if self.score > int(self.highscore):
                open('score.txt', 'w').write(f'{self.score}')
                self.highscore = self.score
            self.score = 0
            self.player_x, self.player_y = 43, 83

        if pyxel.btnp(pyxel.KEY_TAB):  # начало игры по TAB
            pass

    def draw(self):
        pyxel.load("./assets.pyxres")  # загружаем модели

        if self.lvl == 0:
            pyxel.cls(0)
            pyxel.text(20, 50, 'TAB to start!', pyxel.frame_count % 16)
        if self.is_alive:
            if self.lvl in range(1, 13):
                self.background_color()                
            self.draw_guys()
            self.draw_score()
        elif not self.is_alive:
            pyxel.cls(0)
            self.draw_guys()
            self.draw_score()
            self.death_line()

    def background_color(self):
        if self.lvl in range(3):
            pyxel.cls(self.lvl - 1)
        elif self.lvl in range(4, 6):
            pyxel.cls(self.lvl + 1)
        else:
            pyxel.cls(self.lvl + 2)

    def update_enemy(self, x, y):
        if abs(x - self.player_x) < 7 and abs(y - (-self.player_y)) < 7:
            y = 400
            self.is_alive = False
            pyxel.play(1, 1)
        if self.is_alive:
            y -= 2
        elif not self.is_alive:
            y -= 0.2
        if y < -300:
            y += 300
            x = randint(0, 93)
        return x, y

    def update_friend(self, x, y):
        if abs(x - self.player_x) < 7 and abs(y - (-self.player_y)) < 7:
            y = 400
            self.score += 10
            pyxel.play(0, 0)
        if self.is_alive:
            y -= 2
        elif not self.is_alive:
            y -= 0.2

        if y < -300:
            y += 300
            x = randint(0, 93)

        return x, y

    def draw_guys(self):
        pyxel.blt(self.player_x, self.player_y, 0, self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2, 13)  # гг
        for x, y in self.enemy:  # рисуем врагов
            pyxel.blt(x, -y, 0, 0, 7, 7, 13, 13)
        for x, y in self.friend:  # рисуем друзей
            pyxel.blt(x, -y, 0, 7, 7, 13, 13, 13)

    def draw_score(self):
        pyxel.rect(0, 0, 100, 8, 8)
        self.show_score_highscore()

    def show_score_highscore(self):
        s = "{:>1}".format(self.score)
        hs = "{:>1}".format(self.highscore)
        pyxel.text(5, 2, f'SCORE: {s}', 7)
        pyxel.text(60, 2, f'BEST: {hs}', 7)

    def death_line(self):
        pyxel.blt(0, 60, 0, 0, 24, 100, 47, 13)  # death_line
        pyxel.text(10, 65, f'Your score is {self.score}', pyxel.frame_count % 16)
        pyxel.text(25, 75, 'R to Restart', pyxel.frame_count % 16)

    def player_controls(self):
        if self.is_alive:
            # назначаем управление на кнопки, ограничиваем передвижение экраном
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                self.player_x = min(self.player_x + 2, self.width - 7)
                self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 7, 0, 7, 7
            elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                self.player_x = max(self.player_x - 2, 0)
                self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 21, 0, 7, 7
            elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 14, 0, 7, 7
            elif pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
                self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 0, 0, 7, 7
            else:
                self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 0, 0, 7, 7
        else:
            self.player_y = min(self.player_y + 0.3, self.height)

Game()
