import pygame

s = 7
o = s + 2


def draw_one(screen, x, y):
	pygame.draw.circle(screen, (0, 0, 0), (x, y), s)


def draw_two(screen, x, y):
	pygame.draw.circle(screen, (0, 0, 0), (x, y - o), s)
	pygame.draw.circle(screen, (0, 0, 0), (x, y + o), s)


def draw_three(screen, x, y):
	pygame.draw.circle(screen, (0, 0, 0), (x, y - o * 2), s)
	pygame.draw.circle(screen, (0, 0, 0), (x, y), s)
	pygame.draw.circle(screen, (0, 0, 0), (x, y + o * 2), s)


def draw_four(screen, x, y):
	pygame.draw.circle(screen, (0, 0, 0), (x - o, y - o), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o, y - o), s)
	pygame.draw.circle(screen, (0, 0, 0), (x - o, y + o), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o, y + o), s)


def draw_five(screen, x, y):
	pygame.draw.circle(screen, (0, 0, 0), (x - o * 1.5, y - o * 1.5), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o * 1.5, y - o * 1.5), s)
	pygame.draw.circle(screen, (0, 0, 0), (x, y), s)
	pygame.draw.circle(screen, (0, 0, 0), (x - o * 1.5, y + o * 1.5), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o * 1.5, y + o * 1.5), s)


def draw_six(screen, x, y):
	pygame.draw.circle(screen, (0, 0, 0), (x - o * 1.5, y), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o * 1.5, y), s)
	pygame.draw.circle(screen, (0, 0, 0), (x - o * 1.5, y - o * 2), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o * 1.5, y - o * 2), s)
	pygame.draw.circle(screen, (0, 0, 0), (x - o * 1.5, y + o * 2), s)
	pygame.draw.circle(screen, (0, 0, 0), (x + o * 1.5, y + o * 2), s)
