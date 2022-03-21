# structure of given matrices
# [ 1, 2, 3 ]
# [ 4, 5, 6 ]
# [ 7, 8, 9 ]
# flip so that the matrices returned look like:
# [ 1, 4, 7 ]
# [ 2, 5, 8 ]
# [ 3, 6, 9 ]

class Solution:
	def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
		matrix_height = len(matrix)
		matrix_length = len(matrix[0])
		return_structure = []

		for i in range(0, matrix_length):
			current_structure = []
			for i2 in range(0, matrix_height):
				current_structure.append(matrix[i2][i])
			return_structure.append(current_structure)

		return return_structure


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6]]
print(solution.transpose(matrix))
