# currently used to test PyrealEngine
import pygame
from PyrealEngine.shape_manager import ShapeManager

pygame.init()
fhdres = (1000, 700)

screen = pygame.display.set_mode(fhdres)
shape_manager = ShapeManager(screen)
clock = pygame.time.Clock()

rect1 = shape_manager.new_rect(100, 100, 100, 100)

pygame.display.flip()
running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255, 255, 255))

	rect1.increment_x(10, True)

	shape_manager.draw_shapes()
	pygame.display.update()
