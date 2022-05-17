import pygame


class Queue:
	internal: list
	screen: pygame.Surface

	def __init__(self, screen):
		self.internal = []
		self.screen = screen

	def draw(self):
		for i in self.internal:
			i(self.screen)

	def add(self, func):
		self.internal.append(func)

	def remove(self, func):
		self.internal.remove(func)

	def clear(self):
		self.internal = []
