# create a binary search function
def binary_search(ls, item):
	low = 0
	high = len(ls) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = ls[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


# create a DFS function
def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited


# create a binary tree
class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key


# create a function to traverse a binary tree
def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())


def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())


def postorder(tree):
	if tree:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())


def postorder_nonrecursive(tree):
	stack = []
	while tree or stack:
		if tree:
			stack.append(tree)
			tree = tree.getLeftChild()
		else:
			tree = stack.pop()
			tree = tree.getRightChild()


def preorder_nonrecursive(tree):
	stack = []
	while tree or stack:
		if tree:
			print(tree.getRootVal())
			stack.append(tree)
			tree = tree.getLeftChild()
		else:
			tree = stack.pop()
			tree = tree.getRightChild()
