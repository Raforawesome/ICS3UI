# from dataclasses import dataclass
import pygame


class ShapeManager:
	shapes: list = []
	screen = None

	def __init__(self, screen):
		self.shapes = []
		self.screen = screen

	def draw_shapes(self):
		for shape in self.shapes:
			shape.draw(self.screen)

	def destroy_shape(self, shape):
		if shape in self.shapes:
			self.shapes.remove(shape)
		del shape

	def new_rect(self, x, y, width, height, color=(0, 0, 0)):
		new = Rectangle(x, y, width, height, color, self.screen)
		new.manager = self
		self.shapes.append(new)
		return new

	def new_circle(self, x, y, radius, color=(0, 0, 0)):
		new = Circle(x, y, radius, color, self.screen)
		new.manager = self
		self.shapes.append(new)
		return new


class Shape:
	x: int
	y: int
	width: int
	height: int
	color: tuple
	manager: ShapeManager
	gravity_manager = None

	def __init__(self, x, y, color=(0, 0, 0), screen=None):
		self.x = x
		self.y = y
		self.color = color
		self.screen = screen

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return 2 * (self.width + self.height)

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_center(self):
		return self.x + self.width / 2, self.y + self.height / 2

	def set_x(self, x):
		self.x = x

	def increment_x(self, increment, with_bounds=False):
		if not with_bounds:
			self.x += increment
		else:
			if self.x + self.width <= self.screen.get_width() and self.x + increment >= (0 - self.width):
				self.x += increment
			elif self.x + increment < 0:
				self.x = (self.screen.get_width() - self.width) - ((self.x + increment) - self.screen.get_width())
			else:
				self.x = 0 + ((self.x + self.width) - self.screen.get_width())

	def increment_y(self, increment, with_bounds=False):
		if not with_bounds:
			self.y += increment
		else:
			if self.y + self.height <= self.screen.get_height() and self.y + increment >= 0:
				self.y += increment
			elif self.y + increment < (0 - self.height):
				self.y = (self.screen.get_height() - self.height)
			else:
				self.y = 0 + ((self.y + self.height) - self.screen.get_height())

	def set_y(self, y):
		self.y = y

	def set_width(self, width):
		self.width = width

	def increment_width(self, increment):
		self.width += increment

	def set_height(self, height):
		self.height = height

	def increment_height(self, increment):
		self.height += increment

	def move(self, x, y):
		self.x = x
		self.y = y

	def resize(self, width, height):
		self.width = width
		self.height = height

	def redefine(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def set_center(self, center):
		self.x = center[0] - self.width / 2
		self.y = center[1] - self.height / 2

	def contains(self, point):
		return self.x <= point[0] <= self.x + self.width and self.y <= point[1] <= self.y + self.height

	def overlaps(self, other):
		return self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y

	def destroy(self):
		if self in self.manager.shapes:
			self.manager.shapes.remove(self)
		if self.gravity_manager is not None:
			self.gravity_manager.unregister(self)
			self.gravity_manager = None
		del self

	def __str__(self):
		return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"

	def __repr__(self):
		return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"


class Rectangle(Shape):
	def __init__(self, x, y, width, height, color=(0, 0, 0), screen=None):
		self.width = width
		self.height = height
		super().__init__(x, y, color, screen)

	def draw(self, scr):
		pygame.draw.rect(scr, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class Circle(Shape):
	def __init__(self, x, y, radius, color=(0, 0, 0), screen=None):
		super().__init__(x, y, color, screen)
		self.radius = radius
		self.color = color
		self.screen = screen
		self.width = radius
		self.height = radius

	def draw(self, scr):
		pygame.draw.circle(scr, self.color, (self.x, self.y), self.radius)
