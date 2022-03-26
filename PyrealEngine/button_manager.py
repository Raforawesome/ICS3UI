class Button:
	shape = None
	callback = None
	screen = None

	def __init__(self, shape, callback, screen):
		self.shape = shape
		self.screen = screen
		self.callback = callback
