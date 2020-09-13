import pyxel

class Music():
	'''Класс определяющий музыку и звуки'''
	def __init__(self):
		self.play = 0

	def game_music(self):
		'''музыка во время игры 1 канал'''
		return pyxel.play(1, 7, loop=True)
           
	def tab_button_pressed(self):
		'''звук при нажатии на TAB'''
		return pyxel.play(2, 5)

	def death_music(self):
		'''музыка и звук при умирании, столкновении с врагом'''
		return pyxel.play(2, 4), pyxel.play(1, 2)

	def friend_eat_music(self):
		'''звук при съедании друга'''
		return pyxel.play(2, 4)
