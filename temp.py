import pygame, sys, random, time
import dice_draw

pygame.init()

screen = pygame.display.set_mode((600, 400))

# colours
blue = (185, 198, 222)
white = (255, 255, 255)
darkBlue = (97, 131, 171)

# fonts
font1 = pygame.font.Font("ShareTechMono-Regular.ttf", 50)
font2 = pygame.font.Font("ShareTechMono-Regular.ttf", 20)
font3 = pygame.font.Font("ShareTechMono-Regular.ttf", 14)


def roll():
	roll = random.choice([1, 2, 3, 4, 5, 6])
	fn = None
	if roll == 1:
		fn = dice_draw.draw_one
	elif roll == 2:
		fn = dice_draw.draw_two
	elif roll == 3:
		fn = dice_draw.draw_three
	elif roll == 4:
		fn = dice_draw.draw_four
	elif roll == 5:
		fn = dice_draw.draw_five
	elif roll == 6:
		fn = dice_draw.draw_six
	return [roll, fn]


def draw_text(surface, color, text, font, x, y):  # easy text function
	words = font.render(text, 1, color)
	text_rect = words.get_rect()
	text_rect.topleft = (x, y)
	surface.blit(words, text_rect)


def main():
	while True:
		screen.fill(blue)  # clear screen

		mx, my = pygame.mouse.get_pos()  # gets pos of mouse

		# draw menu buttons
		instruction_button = pygame.Rect(40, 320, 160, 50)
		play_button = pygame.Rect(220, 320, 160, 50)
		quit_button = pygame.Rect(400, 320, 160, 50)
		pygame.draw.rect(screen, white, instruction_button, 0, 15)
		pygame.draw.rect(screen, white, play_button, 0, 15)
		pygame.draw.rect(screen, white, quit_button, 0, 15)
		draw_text(screen, white, 'Roll the Dice', font1, 120, 120)
		draw_text(screen, darkBlue, 'Intructions', font2, 60, 332)
		draw_text(screen, darkBlue, 'Play', font2, 278, 332)
		draw_text(screen, darkBlue, 'Quit', font2, 460, 332)

		# play symbol
		# pygame.draw.polygon(screen, darkBlue, [(290,330), (315, 345), (290, 360)])

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if instruction_button.collidepoint((mx, my)):
					instruction_screen()
				if play_button.collidepoint((mx, my)):
					game()
				if quit_button.collidepoint((mx, my)):
					quit()

		pygame.display.update()


def game():
	running = True
	while running:
		screen.fill(blue)  # clear screen

		# back button
		back_button = pygame.Rect(20, 20, 55, 15)
		draw_text(screen, white, '<< Back', font3, 20, 20)

		draw_text(screen, white, 'Roll the Dice', font1, 130, 20)
		draw_text(screen, white, 'Click the dice to roll', font2, 170, 80)

		# game logic

		mx, my = pygame.mouse.get_pos()  # gets pos of mouse

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				running = False
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.collidepoint((mx, my)):
					main()
					else:
					res = roll()
					res[1]()


pygame.display.update()


def instruction_screen():
	running = True
	while running:
		screen.fill(blue)  # clear screen

		# back button
		back_button = pygame.Rect(20, 20, 55, 15)
		draw_text(screen, white, '<< Back', font3, 20, 20)

		# instructions
		draw_text(screen, white, 'Instructions', font1, 140, 20)
		draw_text(screen, white, 'Click the dice with your mouse', font2, 140, 120)
		draw_text(screen, white, 'The program will randomly generate a ', font2, 100, 180)
		draw_text(screen, white, 'number on the dice for you', font2, 150, 210)
		draw_text(screen, white, 'This program can be used in the future', font2, 100, 270)
		draw_text(screen, white, 'to be incorporated in other games', font2, 130, 300)

		mx, my = pygame.mouse.get_pos()  # gets pos of mouse

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				running = False
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.collidepoint((mx, my)):
					main()

		pygame.display.update()


main()