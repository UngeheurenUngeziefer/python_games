import pyxel

class Player():
	def __init__(self):
		self.player_x = 30                      # расположение игрока по х
		self.player_y = 100                     # расположение игрока по у
		self.WIDTH = 160                        # ширина окна
		self.HEIGHT = 120                       # высота окна
		
	def draw_player(self):
		pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 13)             # рисуем гг

	def player_outside(self):
		self.player_x = -10                                          # прячем гг за экран чтобы не набирались очки
		self.player_y = -10

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
