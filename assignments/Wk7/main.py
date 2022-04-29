import pygame
import screens

# initialize pygame
pygame.init()
resolution = (600, 640)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Wk7 - Tahir Chaudhry")

# create our run loop
clock = pygame.time.Clock()
running = True
pygame.display.flip()
while running:
	clock.tick(15)
	# handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	screens.draw_grid(screen, resolution[0], resolution[1], resolution[0] // 8)

	# draw frame
	pygame.display.update()
