import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	# Инициализирует игру и создает объект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)
		)
	pygame.display.set_caption("Alien Invasion")
	# Создание кнопки Play.
	#play_button = Button(ai_settings, screen, "Play")
	# Создание экземпляра для хранения игровой статистики.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	# Создание корабля.
	ship = Ship(ai_settings, screen)
	# Создание группы для хранения пуль.
	bullets = Group()
	aliens = Group()
	# Запуск основного цикла игры.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			bullets.update()
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets)
run_game()
