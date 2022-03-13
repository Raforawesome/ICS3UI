from PyrealEngine.calc import lerp

class Vector3:
	x: int
	y: int
	z: int

	def __init__(self, x: int, y: int, z: int):
		self.x = x
		self.y = y
		self.z = z

	@staticmethod
	def new(*args):
		return Vector3(*args)

	def magnitude(self):
		return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

	def __str__(self):
		return f"Vector3({self.x}, {self.y}, {self.z})"

	def __repr__(self):
		return f"Vector3({self.x}, {self.y}, {self.z})"

	def __add__(self, other):
		return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

	def __mul__(self, other):
		return Vector3(self.x * other, self.y * other, self.z * other)

	def __truediv__(self, other):
		return Vector3(self.x / other, self.y / other, self.z / other)

	def __floordiv__(self, other):
		return Vector3(self.x // other, self.y // other, self.z // other)

	def __mod__(self, other):
		return Vector3(self.x % other, self.y % other, self.z % other)

	def __pow__(self, other):
		return Vector3(self.x ** other, self.y ** other, self.z ** other)

	def __neg__(self):
		return Vector3(-self.x, -self.y, -self.z)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __ne__(self, other):
		return self.x != other.x or self.y != other.y or self.z != other.z

	def __gt__(self, other):
		return self.x > other.x and self.y > other.y and self.z > other.z

	def __ge__(self, other):
		return self.x >= other.x and self.y >= other.y and self.z >= other.z

	def __lt__(self, other):
		return self.x < other.x and self.y < other.y and self.z < other.z

	def __le__(self, other):
		return self.x <= other.x and self.y <= other.y and self.z <= other.z


class Vector2:
	x: int
	y: int

	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	@staticmethod
	def new(*args):
		return Vector2(*args)

	def magnitude(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5

	def normal(self):
		return Vector2(self.x / self.magnitude(), self.y / self.magnitude())

	def dot(self, other):
		return self.normal().x * other.normal().x + self.normal().y * other.normal().y

	# def cross(self, other):
	# 	return Vector2(-self.x, self.y) * other

	def raw(self):
		return self.x, self.y

	def screen_center(self, screen, radius=1):
		return Vector2(screen.get_width() / 2 + self.x - radius / 2, screen.get_height() / 2 - self.y + radius / 2)

	def lerp(self, other, t):
		return Vector2(lerp(self.x, other.x, t), lerp(self.y, other.y, t))

	def __str__(self):
		return f"Vector2({self.x}, {self.y})"

	def __repr__(self):
		return f"Vector2({self.x}, {self.y})"

	def __add__(self, other):
		return Vector2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector2(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return Vector2(self.x * other.x, self.y * other.y)

	def __truediv__(self, other):
		return Vector2(self.x / other, self.y / other)

	def __floordiv__(self, other):
		return Vector2(self.x // other, self.y // other)

	def __mod__(self, other):
		return Vector2(self.x % other, self.y % other)

	def __pow__(self, other):
		return Vector2(self.x ** other, self.y ** other)

	def __neg__(self):
		return Vector2(-self.x, -self.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return self.x != other.x or self.y != other.y

	def __gt__(self, other):
		return self.x > other.x and self.y > other.y

	def __ge__(self, other):
		return self.x >= other.x and self.y >= other.y

	def __lt__(self, other):
		return self.x < other.x and self.y < other.y

	def __le__(self, other):
		return self.x <= other.x and self.y <= other.y
