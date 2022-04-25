# write a function that gets the least common character in a string, returning the one at the highest index if there is a tie
def least_common_char(string):
	char_counts = {}
	for i, char in enumerate(string):
		if char in char_counts:
			char_counts[char][0] += 1
		else:
			char_counts[char] = [1, i]

	highest = max(char_counts.values(), key=lambda x: x[0])[0]
	highest_index = 0
	for k, v in char_counts.items():
		if v[0] < highest or (v[1] > highest_index and v[0] <= highest):
			highest = v[0]
			highest_index = v[1]
	return string[highest_index]


print(least_common_char("aabbccddeeff"))
