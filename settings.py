class Settings:
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.ship_speed = 18
		self.ship_limit = 3

		self.bullet_speed_factor = 40
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 70, 70, 70
		self.bullets_allowed = 7

		self.speedup_scale = 1.75
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		#Alien movement
		self.alien_speed_factor = 10
		self.fleet_drop_speed = 10
		#fleet direction: 1 is right, -1 is left
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)