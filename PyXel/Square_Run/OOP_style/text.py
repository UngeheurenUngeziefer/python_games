import pyxel
from constants import WIDTH, HEIGHT


class Text():
	def __init__(self):
		pass

	def start_text(self):
		pyxel.text(56, HEIGHT // 3, "Welcome to", pyxel.frame_count % 16)   # мигающий текст с координатами
		pyxel.text(37, HEIGHT - HEIGHT // 3, "Press TAB to start!", pyxel.frame_count % 16)

	def final_text(self):
		pyxel.text(58, 21, "GAME OVER!", pyxel.frame_count % 16)
		pyxel.text(37, 81, "Press TAB to Restart!", pyxel.frame_count % 16)
		pyxel.text(45, 91, "Press Q to Quit!", pyxel.frame_count % 16)
		pyxel.blt(58, 55, 0, 0, 0, 38, 16)

	def new_best(self, best_score):
		pyxel.text(46, 31, f"New Best: {best_score}!", pyxel.frame_count % 16)

	def highscore_text(self, score, highscore):
		pyxel.text(46, 31, f"Highscore: {highscore}", pyxel.frame_count % 16)
		pyxel.text(46, 41, f"Your score: {score}", pyxel.frame_count % 16)

	def score_view(self, score):
		pyxel.text(5, 4, "SCORE {:>4}".format(score), 1)
		pyxel.text(4, 4, "SCORE {:>4}".format(score), 7)
