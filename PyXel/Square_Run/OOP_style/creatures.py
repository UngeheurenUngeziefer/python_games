import pyxel
from random import randint

class Creatures():
	def __init__(self):
		'''Определяет атрибуты существ'''
		self.clouds = [(10, 25), (70, 35), (120, 15)]
		self.enemy = [(i * 80, randint(8, 104), True) for i in range(3)]
		self.square = [(i * 60, randint(0, 104), randint(0, 4), True) for i in range(4)]
		
	def clouds_draw(self):
		'''Определяет движение облаков'''
		offset = (pyxel.frame_count // 8) % 160
		for i in range(2):
			for x, y in self.clouds:
				pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)
				pyxel.blt(x + i * 160 - offset, y + 20, 0, 0, 32, 56, 8, 12)
		offset = pyxel.frame_count % 160
		for i in range(2):
			pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

	def enemy_draw(self):
		'''Рисует врагов'''
		for x, y, is_active in self.enemy:
			pyxel.blt(x, y, 0, 0, 16, 24, 8, 13)

	def square_draw(self):
		'''Рисует главного героя'''
		for x, y, kind, is_active in self.square:
			if is_active:
				pyxel.blt(x, y, 0, 16 + kind * 16, 0, 16, 16, 13)
