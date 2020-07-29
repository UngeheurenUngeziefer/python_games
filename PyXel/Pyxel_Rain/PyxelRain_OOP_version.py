import pyxel
from random import randint
from abc import ABC, abstractmethod

class Game:

    def __init__(self):
        self.width, self.height = 100, 100
        self.score = 0
        self.lvl = 0
        self.highscore_file = open('score.txt', 'r').read()
        self.highscore = open('score.txt', 'r').read()
        pyxel.init(self.width, self.height, caption="Pyxel Rain")  # размер окна, название окна
        pyxel.run(self.update, self.draw)                          # запуск программы
        self.is_alive = True

    def width(self):
        return self.width

    def height(self):
        return self.height

    def score(self):
        return self.score

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
            Player.player_controls(Player())
            for i, v in enumerate(NPC.enemy):  # генерируем случайные авто противника
                NPC.enemy[i] = NPC.update_enemy(*v)
            for i, v in enumerate(NPC.friend):  # генерируем случайные авто противника
                NPC.friend[i] = NPC.update_friend(*v)

        if pyxel.btnp(pyxel.KEY_Q):  # выход из игры по Q
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):  # рестарт на R
            pyxel.play(1, 2, loop=True)
            self.lvl = 1
            if self.score > int(self.highscore):
                open('score.txt', 'w').write(f'{self.score}')
                self.highscore = self.score
            self.score = 0

        if pyxel.btnp(pyxel.KEY_TAB):  # начало игры по TAB
            pass

    def draw(self):
        pyxel.load("./assets.pyxres")  # загружаем модели

        if self.lvl == 0:
            pyxel.cls(0)
            pyxel.text(20, 50, 'TAB to start!', pyxel.frame_count % 16)
        if self.is_alive:
            if self.lvl == 1:
                pyxel.cls(0)
            elif self.lvl == 2:
                pyxel.cls(1)
            elif self.lvl == 3:
                pyxel.cls(2)
            elif self.lvl == 4:
                pyxel.cls(5)
            elif self.lvl == 5:
                pyxel.cls(6)
            elif self.lvl == 6:
                pyxel.cls(7)
            elif self.lvl == 7:
                pyxel.cls(9)
            elif self.lvl == 8:
                pyxel.cls(10)
            elif self.lvl == 9:
                pyxel.cls(11)
            elif self.lvl == 10:
                pyxel.cls(12)
            elif self.lvl == 11:
                pyxel.cls(13)
            elif self.lvl == 12:
                pyxel.cls(14)
            elif self.lvl == 13:
                pyxel.cls(15)
            NPC.draw_guys(NPC())
            self.draw_score()
        elif not self.is_alive:
            pyxel.cls(0)
            NPC.draw_guys(NPC())
            self.draw_score()
            self.death_line()

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


class Player:
    def __init__(self):
        self.player_x, self.player_y = 43, 83
        self.is_alive = True
        self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2 = 0, 0, 7, 7  # координаты модели гг

    def coords(self):
        return self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2

    def player_x(self):
        return self.player_x

    def player_y(self):
        return self.player_y



    def player_controls(self):
        if self.is_alive:
            # назначаем управление на кнопки, ограничиваем передвижение экраном
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                self.player_x = min(self.player_x + 2, Game.width(Game()) - 7)
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
            self.player_y = min(self.player_y + 0.3, Game.height(Game()))

class NPC:
    enemy = [(i * 8, randint(0, 300)) for i in range(10)]
    friend = [(i * 8, randint(0, 300)) for i in range(10)]


    def update_enemy(self, x, y):
        if abs(x - Player.player_x(Player())) < 7 and abs(y - (-Player.player_y(Player()))) < 7:
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
        if abs(x - Player.player_x(Player())) < 7 and abs(y - (-Player.player_y(Player()))) < 7:
            y = 400
            Game.score += 10
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
        pyxel.blt(Player.player_x(Player()), Player.player_y(Player()), 0, Player.coords(Player()), 13)  # гг
        for x, y in self.enemy:  # рисуем врагов
            pyxel.blt(x, -y, 0, 0, 7, 7, 13, 13)
        for x, y in self.friend:  # рисуем друзей
            pyxel.blt(x, -y, 0, 7, 7, 13, 13, 13)


Game()

