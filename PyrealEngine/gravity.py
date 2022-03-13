class GravityManager:
	gravity: float = 0.0
	gravity_enabled: bool = False
	screen = None
	shapes: list = []
	bound_to_down: dict = {}

	def __init__(self, screen):
		self.gravity = 0.0
		self.gravity_enabled = True
		self.screen = screen

	def register(self, *shapes):
		for s in shapes:
			self.shapes.append(s)
			s.gravity_manager = self

	def unregister(self, *shapes):
		for s in shapes:
			if s in self.shapes:
				self.shapes.remove(s)
				if s in self.bound_to_down:
					del self.bound_to_down[s]

	def gravity_step(self):
		if self.gravity_enabled:
			for shape in self.shapes:
				y = shape.get_y()
				down_bound = self.screen.get_height() - shape.get_height()
				if y < down_bound:
					shape.set_y(y + self.gravity)
				else:
					shape.set_y(down_bound)
					if shape in self.bound_to_down and shape is not None:
						self.bound_to_down[shape](shape)

	def set_gravity(self, gravity):
		self.gravity = gravity
		return self

	def bind_to_down(self, shape, func):
		self.bound_to_down[shape] = func
