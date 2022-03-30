# an abstraction to make it easier to work with images in pygame

import pygame
import sys


class Image:
	height: int = 0
	width: int = 0
	x: int = 0
	y: int = 0
	image = None
	rect = None
	name = None

	def __init__(self, image_path):
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect()
		self.height = self.rect.height
		self.width = self.rect.width
		self.name = image_path.split('/')[-1]

	def render(self, screen, x=None, y=None):
		x = x or self.x
		y = y or self.y
		screen.blit(self.image, (x, y))

	def resize(self, width, height):
		self.image = pygame.transform.scale(self.image, (width, height))
		self.update()

	def resize_x(self, width):
		self.image = pygame.transform.scale(self.image, (width, self.height))
		self.update()

	def resize_y(self, height):
		self.image = pygame.transform.scale(self.image, (self.width, height))
		self.update()

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self.y = y

	def set_pos(self, x, y):
		self.x = x
		self.y = y

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def update(self):
		self.rect = self.image.get_rect()
		self.height = self.rect.height
		self.width = self.rect.width

	def __call__(self):
		return self.image
