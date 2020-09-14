import pyxel
from random import randint

class Background():
	def __init__(self):
		'''Определяет атрибуты облаков'''
		self.clouds = [(10, 25), (70, 35), (120, 15)]

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

	def color(self, color):
		'''Меняет фон'''
		if color == 'black':
			return pyxel.cls(0)
		elif color == 'grey':
			return pyxel.cls(13)
		else:
			pass
