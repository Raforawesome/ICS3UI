import http


class Array:
	def append(self, obj):
		self.list = [*self.list, obj]

	def prefix(self, obj):
		self.list = [obj, *self.list]

	def search(self, val):
		for v in self.list:
			if val == v:
				return v
		return None

	def binary_search(self, val):
		low = 0
		high = len(self.list) - 1
		while low <= high:
			mid = (low + high) // 2
			if self.list[mid] == val:
				return mid
			elif self.list[mid] < val:
				low = mid + 1
			else:
				high = mid - 1
		return None

	def sort(self):
		self.list.sort()

	def __str__(self):
		return str(self.list)

	def __repr__(self):
		return str(self.list)

	def __getitem__(self, index):
		return self.list[index]

	def __setitem__(self, index, value):
		self.list[index] = value

	def __len__(self):
		return len(self.list)

	def __iter__(self):
		for v in self.list:
			yield v

	def __contains__(self, val):
		return self.search(val) is not None

	def __add__(self, other):
		return Array(*(self.list + other.list))

	def __iadd__(self, other):
		self.list += other.list
		return self

	def __mul__(self, other):
		return Array(*(self.list * other))

	def __imul__(self, other):
		self.list *= other
		return self

	def __eq__(self, other):
		return self.list == other.list

	def __ne__(self, other):
		return not self.__eq__(other)

	def __gt__(self, other):
		return self.list > other.list

	def __lt__(self, other):
		return self.list < other.list

	def __le__(self, other):
		return self.list <= other.list

	def __ge__(self, other):
		return self.list >= other.list

	def __getattr__(self, name):
		return getattr(self.list, name)

	def __setattr__(self, name, value):
		setattr(self.list, name, value)

	def __delattr__(self, name):
		delattr(self.list, name)

	def __delitem__(self, index):
		del self.list[index]

	def len(self):
		return len(self.list)

	def __init__(self, *vals):
		self.list = [*vals]
