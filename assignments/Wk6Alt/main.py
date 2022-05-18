from image_abstraction import Image
import screens
import pygame

mode = "start"  # can either be start, roll, or end


def advance_mode():
    global mode
    if mode == "start":
        mode = "roll"
    elif mode == "roll":
        mode = "end"
    elif mode == "end":
        mode = "start"


pygame.init()
screen = pygame.display.set_mode((800, 600))
(width, height) = screen.get_size()
pygame.display.set_caption("Threes Dice Game")

mode_screens = {
    "start": lambda: screens.start_screen(screen),
}


running = True
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))
    mode_screens[mode]()
    pygame.display.update()
