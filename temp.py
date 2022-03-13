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


def down(shape):
	print("down")
	shape.destroy()


def draw_group():
	for i in range(0, 8):
		r = shape_manager.new_rect((100 * i), 200, 100, 100)
		gravity_manager.register(r)
		gravity_manager.bind_to_down(r, down)


draw_group()

pygame.display.flip()
running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255, 255, 255))

	shape_manager.draw_shapes()
	gravity_manager.gravity_step()
	pygame.display.update()
