# Simple pygame program to test that it is working
# also an example of spacing, commenting and other accepted norms.
# may or may not show to class, depending upon where we are

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 400])

# Run until the user asks to quit
running = True
while running:   # classic keep running until ...

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))   # you should know black, what colour do you want?

    # Draw a solid green circle in the center - but it's not - put it there!
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), 75) # not in centre
    '''OK, so what about an image?
    However, if you want a 32-bit RGBA image, you can also 
    include an optional argument in the Surface constructor. 
    Just add the following line in the code:

    surface = pygame.Surface((600, 400), pygame.SRCALPHA)
    This will create a 600 x 400 image that’s initialized to 
    transparent.  Rendering such an image on a white background 
    will result in what appears to be a blank screen:
    So how about an image, my canoe...
    To load an image from file, there is a simple call to 
    pygame.image.load()

    Check out the following syntax:

    image = pygame.image.load('canoe.jpg')
    replace Replacing the pygame.Surface with the line above - OK now fix it!

    There is a better way - check out the code I'll show you called Ball.

    '''
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
