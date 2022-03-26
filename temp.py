# leetcode problem 51
# N-Queens


class Solution:
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		board = [['.' for _ in range(n)] for _ in range(n)]
		self.result = []
		self.dfs(board, 0)
		return self.result

	def dfs(self, board, row):
		if row == len(board):
			self.result.append([''.join(row) for row in board])
			return
		for col in range(len(board)):
			if self.isValid(board, row, col):
				board[row][col] = 'Q'
				self.dfs(board, row + 1)
				board[row][col] = '.'

	def isValid(self, board, row, col):
		for i in range(len(board)):
			if board[i][col] == 'Q':
				return False
		for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
			if board[i][j] == 'Q':
				return False
		for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
			if board[i][j] == 'Q':
				return False
		return True

	def print_board(self, board):
		for row in board:
			print(row)
		print()
