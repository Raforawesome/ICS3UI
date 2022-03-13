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

	def new_rect(self, x, y, width, height, color=(0, 0, 0)):
		new = Rectangle(x, y, width, height, color, self.screen)
		self.shapes.append(new)
		return new


class Shape:
	x: int
	y: int
	width: int
	height: int
	color: tuple

	def __init__(self, x, y, width, height, color=(0, 0, 0), screen=None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
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
			if self.x + self.width <= self.screen.get_width():
				self.x += increment
			else:
				self.x = 0 + ((self.x + self.width) - self.screen.get_width())

	def increment_y(self, increment, with_bounds=False):
		if not with_bounds:
			self.y += increment
		else:
			if self.y + self.height <= self.screen.get_height():
				self.y += increment
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

	def __str__(self):
		return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"

	def __repr__(self):
		return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"


class Rectangle(Shape):
	def __init__(self, x, y, width, height, color=(0, 0, 0), screen=None):
		super().__init__(x, y, width, height, color, screen)

	def draw(self, scr):
		pygame.draw.rect(scr, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
