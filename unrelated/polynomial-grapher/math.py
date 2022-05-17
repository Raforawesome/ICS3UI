import re


class Polynomial:
	raw = ""
	terms = []

	def __init__(self, raw):
		# expected format: mx + b
		# or ax^2 + bx + c
		# or any other combination of x and coefficients
		self.raw = raw
		self.raw = self.raw.replace(" ", "")
		self.terms = re.split(r"\+|\*|/|-/g", self.raw)
		self.raw.replace("^", "**")

		for term in self.terms:
			if term.find("x^") != -1:
				term = term.replace("x^", "x**")

	# only works on equations with one variable (usually x)
	def get_y_from_x(self, x):
		copy = str(self.raw)
		copy = copy.replace("x", "*" + str(x) + "")
		copy = copy.replace("^", "**")
		return eval(copy)
