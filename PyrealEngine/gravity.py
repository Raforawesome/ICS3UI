class GravityManager:
	gravity: float = 0.0
	gravity_enabled: bool = False
	screen = None
	shapes: list = []

	def __init__(self, screen):
		self.gravity = 0.0
		self.gravity_enabled = True
		self.screen = screen

	def register(self, *shapes):
		for s in shapes:
			self.shapes.append(s)

	def gravity_step(self):
		if self.gravity_enabled:
			for shape in self.shapes:
				y = shape.get_y()
				down_bound = self.screen.get_height() - shape.get_height()
				if y < down_bound:
					shape.set_y(y + self.gravity)
				else:
					shape.set_y(down_bound)

	def set_gravity(self, gravity):
		self.gravity = gravity
		return self
