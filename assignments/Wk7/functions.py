def center_image_to_point(image, x, y):  # returns # position as if the anchor point was 0.5, 0.5
	return x - image.get_width() / 2, y - image.get_height() / 2


def lerp(a, b, i):  # linear interpolation
	return a + (b - a) * i


def bezier(a, b, c, d, i):  # bezier curve (quadratic lerp)
	return lerp(lerp(a, b, i), lerp(c, d, i), i)


def align_to_bound(resolution, image, align_to, bound, div_num=0):  # function to align an image to a bound
	div = resolution[0] // bound
	if align_to == "left":
		return 0 + (div * div_num)
	elif align_to == "right":
		return (div - image.width) + (div * div_num)
	elif align_to == "center":
		return (div / 2) - (image.width / 2) + (div * div_num)
