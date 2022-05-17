from math import Polynomial
from draw import draw_cartesian_plane, draw_polynomial
import pygame


# Settings
EQUATION: str = "1x^2 * 7x + 21 + 90x^3"
SCALE: int = 100
OUTER_LIMIT: int = 10
PRECISION = 0.001
# DON'T TOUCH ANYTHING BELOW THIS LINE

poly = Polynomial(EQUATION)
print(poly.get_y_from_x(2))


pygame.init()

res = (600, 600)
screen = pygame.display.set_mode(res)

clock = pygame.time.Clock()

running: bool = True
pygame.display.flip()
while running:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos())

	screen.fill((255, 255, 255))
	draw_cartesian_plane(screen, 1)
	draw_polynomial(screen, poly, SCALE, OUTER_LIMIT, PRECISION)
	pygame.display.update()
