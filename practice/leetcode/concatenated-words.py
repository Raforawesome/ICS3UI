class Solution:
	def findAllConcatenatedWordsInADict(self, words):
		passed_words = []
		for word in words:
			if is_word_concat(word, words):
				passed_words.append(word)

		return passed_words


solution = Solution()
words = ["cat", "dog", "catdog"]

print(solution.findAllConcatenatedWordsInADict(words))
