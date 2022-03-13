# currently used to test PyrealEngine
import pygame
from PyrealEngine.shape_manager import ShapeManager
from PyrealEngine.gravity import GravityManager
from PyrealEngine.datatypes import Vector2, Vector3

pygame.init()
fhdres = (1000, 700)

screen = pygame.display.set_mode(fhdres)
shape_manager = ShapeManager(screen)
gravity_manager = GravityManager(screen).set_gravity(2)
clock = pygame.time.Clock()

zero = Vector2(0, 0)
left = Vector2(-1 * (screen.get_width() / 4), 0)
right = Vector2(screen.get_width() / 4, 0)
up = Vector2(0, (screen.get_height() / 4))
down = Vector2(0, -1 * (screen.get_height() / 4))


def draw_vector(vector, radius=1):
	shape_manager.new_circle(vector.screen_center(screen).x, vector.screen_center(screen).y, radius)


draw_vector(zero, 2)
draw_vector(left, 2)
draw_vector(right, 2)
draw_vector(up, 2)
draw_vector(down, 2)


# pygame.display.flip()
# running = True
# while running:
# 	clock.tick(60)
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
#
# 	screen.fill((255, 255, 255))
#
# 	shape_manager.draw_shapes()
# 	pygame.display.update()
