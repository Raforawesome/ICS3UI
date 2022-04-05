# Create a function that draws the top half of a Yahtzee screen
import os

import pygame
import image_abstraction
import functions as fns
import dice_draw as ddraw

images = {image_name: image_abstraction.Image("images/" + image_name) for image_name in [i for i in os.listdir('images') if i.endswith('.png')]}


def fn_from_roll(n):
	if n == 1:
		return ddraw.draw_one
	elif n == 2:
		return ddraw.draw_two
	elif n == 3:
		return ddraw.draw_three
	elif n == 4:
		return ddraw.draw_four
	elif n == 5:
		return ddraw.draw_five
	elif n == 6:
		return ddraw.draw_six


def start_screen():
	start_button = images['start_button.png']


def draw_grid(screen, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE):
	offset = screen.get_width() // 5
	"""Draw the grid of the Yahtzee game"""
	# Set the screen background
	screen.fill((255, 255, 255))
	# Draw the grid lines
	for x in range(0, WINDOW_WIDTH, CELL_SIZE):  # draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (x, 0 + offset), (x, WINDOW_HEIGHT))
	for y in range(0, WINDOW_HEIGHT, CELL_SIZE):  # draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (0, y + offset), (WINDOW_WIDTH, y + offset))
