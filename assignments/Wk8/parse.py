def parse_file(filename: str) -> dict:
	definitions = {}
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			# if a semicolon comes before a comma, split file by first semicolon
			# otherwise split file by first comma
			if ';' in line and line.find(';') < ("," in line and line.find(',') or len(line)):
				vals = line.split(";")
				definitions[vals[0].strip()] = vals[1].strip()
			else:
				vals = line.split(",")
				definitions[vals[0].strip()] = vals[1].strip()

	return definitions
