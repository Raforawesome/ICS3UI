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
		
	def len(self):
		return len(self.list)
				
	def __init__(self, *vals):
		self.list = [*vals]
