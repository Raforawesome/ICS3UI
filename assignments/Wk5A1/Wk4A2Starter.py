"""
Wk 5 - Assignment 1
Author: Raforawesome
Due Date: Mar 10, 2022 11:59 PM
Question or problem: PyGame - Moving Shapes
Class: ICS3UI-02
"""
# import and initialize the pygame library
import pygame
import sys  # don't need these yet, but frequently do, so it's in the template
import random

# initializing the constructor
pygame.init()


def colour(frm, to):  # get a random colour
	guess = random.randint(frm, to)
	return guess  # return the number


def where(WIDTH, HEIGHT):  # gives a random coordinate
	coord1 = WIDTH - random.randint(0, WIDTH)
	coord2 = HEIGHT - random.randint(0, HEIGHT)
	return coord1, coord2  # return the x, y coordinates


# screen resolution, width , height
res = (700, 550)  # this is my preferred setting at home, change to WVD friendly
fhdres = (1000, 700)  # for testing on 4k screens (used for development)
wvd = (400, 300)  # at least this seems to work when I tried it!
mode = ""
# ask our user what resolution they want
while mode == "":
	print("What resolution would you like to use?")
	print("1. Standard (700x550)")
	print("2. Full HD (1000x700)")
	print("3. Widescreen (400x300)")
	print("4. Exit")
	choice = input("Please enter your choice: ")
	if choice == "1":
		mode = res
	elif choice == "2":
		mode = fhdres
	elif choice == "3":
		mode = wvd
	elif choice == "4":
		sys.exit()
	else:
		print("That's not a valid choice. Please try again.")

# opens up a window
screen = pygame.display.set_mode(mode == res and res or mode == fhdres and fhdres or wvd)

# white color
WHITE = (255, 25, 255)

# light shade of the button
color_light = (100, 100, 170)

# dark shade of the button
color_dark = (200, 100, 200)

# random colour
newColour = pygame.Color(colour(1, 255), colour(1, 255), colour(100, 255))

# defining a font
smallfont = pygame.font.SysFont("JetBrains Mono", 25)

# setting a caption
pygame.display.set_caption("Wk 5 Assignment 1 - Raforawesome")

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# rendering a text written in
# this font
text = smallfont.render('quit', True, color_light)

# speed would be added here or a timer
speed = 1

# add a graphic
wrench = pygame.image.load('wrench-downscaled.png')

# - notice the size of your graphic and add it into the width and height
# set up size too
imgX = 0
imgMaxX = width - wrench.get_width()
imgY = height - wrench.get_height()
reverse_debounce = False


# set up the image or images for use
def myImage(w, h):
	screen.blit(wrench, (w, h))


# function to draw a random shape
def drawShape():
	rand_int = random.randint(1, 4)
	if rand_int == 1:
		pygame.draw.circle(screen, (colour(1, 255), colour(1, 255), colour(1, 255)), where(width, height), random.randint(1, 100))
	elif rand_int == 2:
		pygame.draw.rect(screen, (colour(1, 255), colour(1, 255), colour(1, 255)), (where(width, height), (random.randint(1, 100), random.randint(1, 100))))
	elif rand_int == 3:
		pygame.draw.polygon(screen, (colour(1, 255), colour(1, 255), colour(1, 255)), (where(width, height), (random.randint(1, 100), random.randint(1, 100)), (random.randint(1, 100), random.randint(1, 100)), (random.randint(1, 100), random.randint(1, 100))))
	elif rand_int == 4:
		pygame.draw.ellipse(screen, (colour(1, 255), colour(1, 255), colour(1, 255)), (where(width, height), (random.randint(1, 100), random.randint(1, 100))))


# flip the display so it renders nicely
pygame.display.flip()

running = True  # better than while True, because you can close down nicely
while running:
	pygame.display.set_caption("Wk 5 Assignment 1 - Raforawesome")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			running = False  # allows for nice close and no error
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:  # if the mouse is clicked
			mouse = pygame.mouse.get_pos()  # get the mouse position
			# if the mouse is within the bounds of the text
			if (width - text.get_width() - 10) < mouse[0] < (width - text.get_width() - 10 + text.get_width()) and 10 < mouse[1] < 10 + text.get_height():
				pygame.quit()

	# fills the screen with white, so you can see what is added
	screen.fill((255, 255, 255))

	# put a solid circle in the center of your screen using width, and height properly, not a number, a calculation
	# colour, width, height, radius
	pygame.draw.circle(screen, (colour(1, 255), colour(1, 255), colour(100, 255)), where(width, height), 50)
	# ADJUST THIS so that the circle STAYS on the screen and begins filling the screen.

	if imgX + 1 < imgMaxX and reverse_debounce is False:  # if the image is not at the end of the screen
		myImage(imgX, imgY)
		imgX += 1
	elif imgX + 1 >= imgMaxX:  # reverse the direction of the image
		reverse_debounce = True
		myImage(imgX, imgY)
		imgX -= 1
	elif imgX - 1 == 1 or imgX == 1:  # un-reverse the direction of the image
		reverse_debounce = False
		myImage(imgX, imgY)
		imgX += 1
	else:  # generic edge case handler (keep going in reverse)
		myImage(imgX, imgY)
		imgX -= 1
	mouse = pygame.mouse.get_pos()  # get the mouse position

	'''
	# now your turn...
	# add a few lines
	

	# add some rectangles
	


	# add some ellipses (ovals), using a rectangle as the outside boundaries
	
	
	# draw some triangles using the polygon command
	
	
	
	# Draw an arc or two or three (IE: Moon, smile for a happy face etc.)

	'''

	# change the color of the button when the mouse is over it
	if (width - text.get_width() - 10) < mouse[0] < (width - text.get_width() - 10 + text.get_width()) and 10 < mouse[1] < 10 + text.get_height():
		text = smallfont.render('quit', True, color_dark)
	else:
		text = smallfont.render('quit', True, color_light)

	# render quit button
	screen.blit(text, (width - text.get_width() - 10, 10))

	# draw 3 random shapes
	for i in range(3):
		drawShape()

	# updates the frames of the game
	pygame.display.update()
pygame.quit()
