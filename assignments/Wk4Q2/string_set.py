"""
Assignment Question 4/2
Author: Raforawesome
Due Date: Mar 5, 2022 11:59 PM
Question or problem: Week 4 Question 2 - String Sets
Class: ICS3UI-02
"""


def string_set(a_list):
	element_count = {}  # initialize a dictionary to keep track of element counts

	for e in a_list:
		if e in element_count.keys():  # if element doesn't exist, adding will cause an error
			element_count[e] += 1  # add to it if it does exist
		else:
			element_count[e] = 1  # if it doesn't exist, presume 0 and set to 1

	duplicates = []  # store our duplicates
	for _, k in enumerate(
			element_count.keys()):  # technically redundant but enumerated loops are idiomatic across every programming language
		v = element_count[k]  # get count of current value
		if v > 1:  # if element appeared more than once in the above loop
			duplicates.append(k)  # add to our duplicates list

	return {*duplicates}  # unpack the list and return it as a set


def only_set(a_list):
	element_count = {}  # once again, dictionary to keep track

	for e in a_list:  # when we encounter an element
		if e in element_count.keys():  # if we have seen it before,
			element_count[e] += 1  # add one to its current count
		else:  # if it doesn't exist,
			element_count[e] = 1  # set it to 1

	uniques = []  # to keep track of how many uniques we encountered
	for _, k in enumerate(element_count.keys()):  # again, using an enumerated loop
		v = element_count[k]  # get the count of a word
		if v == 1:  # if we have encountered it exactly one time
			uniques.append(k)  # add it to our list of uniques

	return {*uniques}  # unpack unique and return as set
