def str_set(a_list):
	list_clone = a_list  # arguments are immutable; we must clone it
	for e in a_list:
		if e in list_clone:
			list_clone.remove(e)

	return set(list_clone)


list1 = ["a", "a", "b", "b", "c"]
print(str_set(list1))
