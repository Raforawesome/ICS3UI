import pygame


def anchor_center(screen, x, y):
	[height, width] = screen.get_size()
	[offset_x, offset_y] = [width / 2, height / 2]
	return x + offset_x, y + offset_y


def apply_scale(x, y, scale):
	return x / scale, y / scale

