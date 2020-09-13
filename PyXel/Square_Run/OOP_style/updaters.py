import pyxel
from creatures import Creatures
from player import Player

class Updater(Creatures):
	def __init__(self):
		super().__init__()

	def enemy_counter(self):
		for i, v in enumerate(self.enemy):
			self.enemy[i] = self.update_enemy(*v)

	def square_counter(self):
		for i, v in enumerate(self.square):
			self.square[i] = self.update_square(*v)

	def update_enemy(self, x, y, is_active):
        # Столкновение с игроком
		if is_active and abs(x - Player().player_x) < 12 and abs(y - Player().player_y) < 12:
			Music().death_music()
			self.start_game = 2                             # Игра окончена
		x -= 4                       # скорость полёта врагов (шаг по х)
		if x < -40:                  # враги пропадают за экраном в минусе по х и появляются справа за экраном
			x += 240
			y = randint(8, 104)
		return x, y, is_active

	def update_square(self, x, y, kind, is_active):
		# если мы сталкиваемся с другом
		if is_active and abs(x - Player().player_x) < 12 and abs(y - Player().player_y) < 12:
			is_active = False
			self.score += (kind + 1) * 100                   # +100 очков за квадрат, +200 за прямоуг., +300 за треуг.
		x -= 2
		if x < -40:
			x += 240
			y = randint(0, 104)
			kind = randint(0, 2)
			is_active = True
		return x, y, kind, is_active
