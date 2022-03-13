# functions related to calculations for games

def lerp(a, b, i):
	return a + (b - a) * i


def bezier(a, b, c, d, i):
	return lerp(lerp(a, b, i), lerp(c, d, i), i)
