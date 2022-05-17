import pygame
from translate import apply_scale, anchor_center

colors = {
	"black": (0, 0, 0)
}


def draw_cartesian_plane(screen, width=1):
	res: (int, int) = (screen.get_width(), screen.get_height())
	[x, y] = res
	offset: int = width // 2
	mid_x: int = x // 2
	mid_y: int = y // 2
	pygame.draw.line(screen, colors["black"], (mid_x + offset, 0), (mid_x + offset, y), width)
	pygame.draw.line(screen, colors["black"], (0, mid_y + offset), (x, mid_y + offset), width)


def plot(screen, x, y, scale):
	pygame.draw.circle(screen, colors["black"], (x, y), 1)


def plot_all(screen, points, scale):
	for point in points:
		plot(screen, point[0], point[1], scale)


def calculate_point(screen, x, y, scale):
	scaled = apply_scale(x, y, scale)
	anchored = anchor_center(screen, scaled[0], scaled[1])
	[true_x, true_y] = anchored
	return true_x, true_y


def draw_polynomial(screen, polynomial, scale, limit, precision):
	points = []
	for x in range(-(int(limit * 1000)), int(limit * 1000), int(precision * 1000)):
		real_x = x / 1000
		y = polynomial.get_y_from_x(real_x)
		points.append(calculate_point(screen, x, y, scale))
	plot_all(screen, points, scale)
