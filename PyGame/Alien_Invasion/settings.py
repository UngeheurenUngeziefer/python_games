class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""
	def __init__(self):
		"""Инициализирует настройки игры."""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5
		# Параметры пули
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		# Настройки пришельцев
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 20
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1
		self.bullet_speed_factor = 3
		self.ship_limit = 3
		# Подсчет очков
		self.alien_points = 50
		# Темп роста стоимости пришельцев
		self.score_scale = 1.5
		# Темп ускорения игры
		self.speedup_scale = 1.1

	def increase_speed(self):
		"""Увеличивает настройки скорости и стоимость пришельцев."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
