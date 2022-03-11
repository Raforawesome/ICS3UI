# Simple pygame program to test that it is working
# also an example of spacing, commenting and other accepted norms.
# You used this to test that your install was OK.

# Import and initialize the pygame library
import pygame
import sys

pygame.init()

# screen resolution, width, height
res = (700, 550)  # this is for PC at home
schScr = (600, 400)

# colours being used
color = (100, 100, 170)

# Set up the drawing window
screen = pygame.display.set_mode(res)

# define a font - you can change this too
smallfont = pygame.font.SysFont('Talhoma', 35)

# text - with the font
text = smallfont.render('quit', True, color)

# speed would go here, possibly Clock variables


# setting up a caption - you should change this
capt = "Ms. H Example"

# set up the screen width and height in a variables
width = screen.get_width()
height = screen.get_height()

# add a graphic
canoe = pygame.image.load('canoe.jpeg')
# set up the size too
canWid = width - 600
canHei = height - 280


def myImage():
	screen.blit(canoe, (canWid, canHei))  # this won't be pretty yet.


# Run until the user asks to quit
running = True
while running:  # classic keep running until ...
	pygame.display.set_caption(capt)  # give a title at the top.

	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Fill the background with white
	screen.fill((100, 100, 100))  # you should know black, what colour do you want?

	# Draw a solid green circle in the center - but it's not - put it there!
	pygame.draw.circle(screen, (0, 255, 0), (250, 250), 75)  # not in centre

	# add the canoe
	myImage()

	# Flip the display
	pygame.display.flip()
	pygame.display.update()

# Done! Time to quit.
pygame.quit()
