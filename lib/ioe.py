# filesystem related lib functions
import sys


def DictToCSV(d, file_name):
	try:
		final = ""

		for i, k in enumerate(d.keys()):
			v = d[k]
			final = final + f'{v},{k}\n'

		sys_out = open(file_name, "rw")
		sys_out.write(final)
		sys_out.close()
	except:
		return False
	else:
		return True


def CSVToDict(filename):
	l = {}

	file = open(filename, 'r')
	lines = file.read().splitlines()
	file.close()

	for i, v in enumerate(lines):
		to_add = []

		elements = v.split(',')
		for _, e in enumerate(elements):
			to_add = [*to_add, e.replace('"', '')]

		l[i] = to_add

	return l
