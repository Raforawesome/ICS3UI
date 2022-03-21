def is_concat(w, words):
	for i in range(1, len(w) + 1):
		prefix = w[:i]
		suffix = w[i:]
		if prefix in words and suffix in words:
			return True
		elif prefix in words and is_concat(suffix, words):
			return True
		elif suffix in words and is_concat(prefix, words):
			return True


class Solution:
	def findAllConcatenatedWordsInADict(self, words):
		to_return = []
		for word in words:
			if is_concat(word, words):
				to_return.append(word)
		return to_return


solution = Solution()
words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

print(solution.findAllConcatenatedWordsInADict(words))
