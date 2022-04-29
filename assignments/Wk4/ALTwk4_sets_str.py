"""
Assignment Question 4/2
Author: Raforawesome
Due Date: Mar 5, 2022 11:59 PM
Question or problem: Week 4 Question 2 - String Sets
Class: ICS3UI-02
"""
from string_set import string_set, only_set

list1 = []
list2 = [20, 21]
list3 = ["a", "a"]
list4 = ["3", "7", "7"]
list5 = ["apple", "bananna", "cantelope", "banana"]
list6 = ["Canada", "United States", "Mexico", "Bahamas", "Canada", "Bahamas", "Mexico", "Bahamas", "Canada"]
list7 = ["computer", "laptop", "computer", "laptop", "Macbook", "computer", "laptop"]
list8 = [7, 7, -7, -7, 7, 7, -7, -7, 0]

tests = [list1, list2, list3, list4, list5, list6, list7, list8]

for t in tests:
	output = string_set(t)
	if len(output) == 0:
		output = "{}"
	print("The duplicate strings in", t, "are", output)
for i in tests:
	output = only_set(i)
	if len(output) == 0:
		output = "{}"
	print("The unique strings in", i, "are", output)
