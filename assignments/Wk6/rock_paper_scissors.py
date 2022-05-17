"""
Practice Problem, Week 6 Assignment 1: Rock Paper Scissors
Author: Raforawesome
Due Date: Mar 26, 2022 11:59 PM
Question or problem: Wk6 Rock Paper Scissors
Class: ICS3UI-02
"""

# Program to play rock paper scissors in pygame
import os
import pygame
import random
import time
import image_abstraction
random.seed(time.time())

# resolution selection
resolution = (1000, 1000)  # resolution of the game
fhd = (1000, 700)  # full HD resolution
small = (800, 600)  # small resolution
selected_resolution = ""  # variable to hold the resolution
while selected_resolution == "":  # input loop to gather a selection choice
	print("Please select a resolution:")
	print("1. Full HD")
	print("2. Small")
	print("3. Quit")
	selected_resolution = input("")
	if selected_resolution == "1":
		resolution = fhd
	elif selected_resolution == "2":
		resolution = small
	elif selected_resolution == "3":
		exit()
	else:
		selected_resolution = ""

image_scale = resolution[0] // 6

# initialize pygame & variables
pygame.init()  # initializes pygame
screen = pygame.display.set_mode(resolution)  # set the screen resolution
pygame.display.set_caption("Rock Paper Scissors")  # set the title of the window

clock = pygame.time.Clock()  # create a clock object

image_names = [i for i in os.listdir("images/")]  # get a list of all the images in the images folder
images = {i.split(".")[0]: image_abstraction.Image("images/" + i) for i in image_names}  # create a list of image objects
scissors_open = False  # variable to hold the state of the scissors
animate_scissors_for_iterations = 0  # internal counter variable
skipped_frames = 10  # how many frames per state switch
picked = ""  # variable to hold the player's choice


# set up our images
def get_image(name):  # Time complexity O(n) but there are no better options
	for i in images:
		if i.name == name:
			return i


exceptions = ["scissors_open", "scissors_closed", "title", "start_button", "quit_button", "restart_button", "rock_wins", "paper_wins", "scissors_wins"]  # list of exceptions to rps renders


def render_rps():  # function to render images based on the state of scissors_open
	to_render = [images[i] for i in images.keys() if i not in exceptions]  # get a list of all the images that are not exceptions
	if scissors_open is True:  # if scissors are open
		to_render.append(images["scissors_open"])  # add the scissors open image to the list of images to render
	else:  # if scissors are closed
		to_render.append(images["scissors_closed"])  # add the scissors closed image to the list of images to render
	for i in to_render:  # render all the images
		i.render(screen)

# set up a rendering order for the images
rps_render_order = [
	"title_rc",
	"start_button",
	"quit_button",
	"scissors_closed",
	"scissors_open",
]

def get_order(filename):
	return rps_render_order.index(filename)

def setorder(filename, order):
	rps_render_order[rps_render_order.index(filename)] = order


# sizing and positioning functions
def center_image_to_point(image, x, y):  # returns position as if the anchor point was 0.5, 0.5
	return x - image.get_width() / 2, y - image.get_height() / 2


def lerp(a, b, i):  # linear interpolation
	return a + (b - a) * i


def bezier(a, b, c, d, i):  # bezier curve (quadratic lerp)
	return lerp(lerp(a, b, i), lerp(c, d, i), i)


def align_to_bound(image, align_to, bound, div_num=0):  # function to align an image to a bound
	div = resolution[0] // bound
	if align_to == "left":
		return 0 + (div * div_num)
	elif align_to == "right":
		return (div - image.width) + (div * div_num)
	elif align_to == "center":
		return (div / 2) - (image.width / 2) + (div * div_num)


def resize_horizontal(img):  # function to resize rps images to fit the screen (horizontal: scissors)
	outer_bound = resolution[0] // 6  # gap between images and the edge of the screen
	inner_bound = resolution[0] // 12  # gap between images and each other
	workspace = resolution[0] - outer_bound * 2  # real space for the images to be rendered in
	# width = abs(workspace / 3 - inner_bound * 3)  # width of the images
	width = resolution[0] // 6  # width of the images
	height = abs(width * (img.height / (img.name != "scissors_closed.png" and img.width or 643)))  # exception to keep our scissor images the name size
	img.resize(int(width), int(height))  # resize the image


scene = "start"

# pre-compute some positions to reduce calculations done in loops
timg = images["title_rc"]

title_scale_x = 2 * resolution[0] // 3  # scale the title image to fit the screen
title_scale_y = resolution[0] // 10  # scale the title image to fit the screen
button_scale_x = resolution[0] // 5  # scale the button images to fit the screen
button_scale_y = resolution[0] // 8  # scale the button images to fit the screen

timg.resize(title_scale_x, title_scale_y)  # resize the title image
title_y = (resolution[1] // 5) - timg.height // 2  # calculate the y position of the title image
title_x = center_image_to_point(timg, resolution[0] // 2, title_y)[0]  # calculate the x position of the title image
timg.set_pos(title_x, title_y)  # set the position of the title image

click_events = {}


def register_click_event(name, img, callback, scr):
	if name in click_events.keys():
		del click_events[name]
	x1 = img.x
	y1 = img.y
	x2 = img.x + img.width
	y2 = img.y + img.height
	click_events[name] = [{"x": [x1, x2], "y": [y1, y2]}, callback, scr]


def advance_screen():
	global scene
	if scene == "start":
		scene = "pick"
	elif scene == "pick":
		scene = "end"
	elif scene == "end":
		scene = "start"


def o_quit():
	pygame.quit()
	exit()


def start_screen():
	img = images["title_rc"]
	sb = images["start_button"]
	qb = images["quit_button"]
	img.render(screen, title_x, title_y)  # render title

	# render buttons
	sb.resize(button_scale_x, button_scale_y)
	qb.resize(button_scale_x, button_scale_y)
	sb.set_x(align_to_bound(sb, "right", 3))
	qb.set_x(align_to_bound(qb, "left", 3, 2))
	sb.set_y(resolution[1] - sb.height - (resolution[1] // 10) * 2)
	qb.set_y(resolution[1] - qb.height - (resolution[1] // 10) * 2)
	sb.render(screen)
	qb.render(screen)
	register_click_event("start", sb, advance_screen, "start")
	register_click_event("quit", qb, o_quit, "start")


# only do resize once, outside looped function
r = images["rock"]
p = images["paper-original"]
so = images["scissors_open"]
sc = images["scissors_closed"]

resize_horizontal(r)
resize_horizontal(p)
resize_horizontal(so)
resize_horizontal(sc)
r.set_y(resolution[1] - r.height - (resolution[1] // 10) * 2)
p.set_y(resolution[1] - p.height - (resolution[1] // 10) * 2)
so.set_y(resolution[1] - so.height - (resolution[1] // 10) * 2)
sc.set_y(resolution[1] - sc.height - (resolution[1] // 10) * 2)

def pick_rock():
	global picked
	advance_screen()
	picked = "rock"

def pick_paper():
	global picked
	advance_screen()
	picked = "paper"

def pick_scissors():
	global picked
	advance_screen()
	picked = "scissors"


def pick_screen():
	global r, p, so, sc
	title = images["title_rc"]

	# render images
	title.render(screen, title_x, title_y)
	r.set_x(align_to_bound(r, "center", 3, 0))
	p.set_x(align_to_bound(p, "center", 3, 1))
	so.set_x(align_to_bound(so, "center", 3, 2))
	sc.set_x(align_to_bound(sc, "center", 3, 2))
	register_click_event("rock", r, pick_rock, "pick")
	register_click_event("paper", p, pick_paper, "pick")
	register_click_event("scissors", sc, pick_scissors, "pick")
	render_rps()


# choose a random value out of "rock", "paper", or "scissors" for the bot to pick
bot_img = None
img = None
moved = False
winner = None
winner_img = None
rendered_quit = False
move = None

rb = images["restart_button"]
qb = images["quit_button"]


def restart():
	global scene, moved
	scene = "start"
	moved = False
	winner = None
	plr_img = None

def end_screen():
	global picked, img, winner, moved, rendered_quit, qb, rb, bot_img
	if img is None:
		if picked == "rock":
			img = images["rock"]
		elif picked == "paper":
			img = images["paper-original"]
		elif picked == "scissors":
			img = images["scissors_closed"]
		img.set_y(resolution[1] - img.height - (resolution[1] // 10) * 3.25)
		img.set_x(align_to_bound(img, "right", 3))
	if winner is None:
		bot_pick = random.choice(["rock", "paper", "scissors"])
		if bot_pick == "rock":
			bot_img = image_abstraction.Image("images/rock.png")
		elif bot_pick == "paper":
			bot_img = image_abstraction.Image("images/paper-original.png")
		elif bot_pick == "scissors":
			bot_img = image_abstraction.Image("images/scissors_closed.png")
		resize_horizontal(bot_img)
		bot_img.set_x(align_to_bound(bot_img, "left", 3, 2))
		bot_img.set_y(resolution[1] - bot_img.height - (resolution[1] // 10) * 3.25)
		to_win = {
			"rock": "paper",
			"paper": "scissors",
			"scissors": "rock"
		}
		if bot_pick == to_win[picked]:
			winner = "bot"
		elif picked == to_win[bot_pick]:
			winner = "player"
		else:
			winner = "tie"
		print(winner)

	# render images
	img.render(screen)
	bot_img.render(screen)
	# qb.render(screen)
	rb.render(screen)
	qb.resize(button_scale_x, button_scale_y)
	rb.resize(button_scale_x, button_scale_y)
	qb.set_x(align_to_bound(qb, "left", 3, 2))
	qb.set_y(resolution[1] - qb.height - (resolution[1] // 10) * 0.5)
	rb.set_x(align_to_bound(rb, "right", 3))
	rb.set_y(resolution[1] - rb.height - (resolution[1] // 10) * 0.5)
	register_click_event("quit", qb, o_quit, "end")
	register_click_event("restart", rb, restart, "end")


# Structure:
# screen_name : [screen_function, [x pos, y pos, function_when_clicked_between_x_and_y]]
screen_refs = {
	'start': [start_screen],
	'pick': [pick_screen],
	'end': [end_screen]
}


# variables and functions related to the loops
running = True
pygame.display.flip()
fps = 30
elapsed = 0  # internal timer


def update_scissors():
	global scissors_open
	global animate_scissors_for_iterations
	global skipped_frames
	global elapsed
	if animate_scissors_for_iterations > 0:
		elapsed += 1
		if elapsed >= skipped_frames:
			animate_scissors_for_iterations -= 1
			scissors_open = not scissors_open
			elapsed = 0
	elif animate_scissors_for_iterations == 0:
		elapsed += 1
		if elapsed >= skipped_frames:
			scissors_open = False
			elapsed = 0
		scissors_open = False


while running:  # only run program while our user wants to
	clock.tick(fps)  # set the clock to our fps variable
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False  # quit the game
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for event_name in click_events.keys():
				v = click_events[event_name]
				if v[0]["x"][0] <= event.pos[0] <= v[0]["x"][1] and v[0]["y"][0] <= event.pos[1] <= v[0]["y"][1]:
					if v[2] == scene:
						v[1]()  # call the callback function
						break  # break out of the loop (prevents unneeded iterations)

	screen.fill((255, 255, 255))  # fill the screen with white

	# render screens
	if scene == "start":
		screen_refs['start'][0]()
	elif scene == "pick":
		screen_refs['pick'][0]()
	elif scene == "end":
		screen_refs['end'][0]()

	pygame.display.update()  # update the display
	update_scissors()
