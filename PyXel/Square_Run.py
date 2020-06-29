import pyxel

# класс определения позиции
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class ImagePosition:
    def __init__(self, x, y):
        self.pos = Position(x, y)

# класс квадрата
class Square:
    def __init__(self, img_id):
        self.pos = Position(0, 80)
        self.size_y = 10
        self.size_x = 10
        self.img_square = img_id
        self.get_image = ImagePosition(0, 0)
        self.color_tr = 0

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

# класс треугольника
class Triangle:
    def __init__(self, img_id):
        self.pos = Position(0, 0)
        self.size_y = 10
        self.size_x = 7
        self.speed = -0.2
        self.img_square = img_id
        self.get_image = ImagePosition(0, 16)
        self.color_tr = 2

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

class App:
    def __init__(self):
        self.IMG_ID0 = 0                              # id картинки
        WIDTH = 160
        HEIGHT = 120

        pyxel.init(WIDTH, HEIGHT, caption='Square_Run')    # запуск окна, его ширина, высота и название
        pyxel.load(r'pyxel\triangle.pyxres')          # загрузка tilemap
        pyxel.image(1).load(0, 0, 'background.png')   # загрузка фона

        self.square = Square(self.IMG_ID0)
        self.x = 20              # положение квадрата х
        self.y = 80              # положение квадрата у

        self.triangles = []                  # список с треугольниками
        self.platforms = []                  # список с платформами
        pyxel.run(self.update, self.draw)    # запуск игры

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):          # Q выход из игры
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_SPACE):
            self.square.update(self.square.pos.x, self.square.pos.y+10)

        triangle_count = len(self.triangles)
        if triangle_count < 2:
            new_triangle = Triangle(self.IMG_ID0)

        for triangle in range(triangle_count):
            self.Triangle[triangle].update(self.Triangle[triangle].pos.x + self.Triangles[triangle].speed, self.Triangles[triangle].pos.y)



    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 1, 0, 0, 160, 120, 0)       # фон
        pyxel.blt(self.square.pos.x, self.square.pos.y, self.square.img_square, self.square.get_image.pos.x, self.square.get_image.pos.y, 0, 80, colkey=-1)




App()
