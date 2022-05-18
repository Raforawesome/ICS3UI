from image_abstraction import Image
import pygame
import os

image_names = [i for i in os.listdir("images/")]  # get a list of all the images in the images folder
images = {i.split(".")[0]: Image("images/" + i) for i in image_names}  # create a list of image objects


# resizing images
# assume res is 800, 600
width = 800
height = 600

title = images["threes"]
title.resize(197 * 2, 50 * 2)
title.set_x(width / 2 - title.get_width() / 2)
title.set_y(height / 5 - title.get_height() / 2)

start = images["start_button"]
(start_width, start_height) = start.get_size()
start.resize(start_width * 0.8, start_height * 0.8)
start.set_pos(
    width // 15,
    (height - start.get_height()) - height // 8,
)


def start_screen(screen):
    title.render(screen)
    start.render(screen)
