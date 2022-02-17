"""
Assignment Question 1/2
Author: Raforawesome
Due Date: Feb 14, 2022 11:59 PM
Question or problem: Week 1 Question 2 - Gregorian Calendar Dates to Julian
Class: ICS3UI-02
"""
# NOTE: This program displays the Gregorian date as YYYY-MM-DD, which is the officially recommended Canadian format.

print("This program calculates the Julian date float from any valid post-BC year.")

# overcomplicated way to accept multiple variations of yes
affirmatives = ["y", "yes", "true", "positive"]

print("Would you like to continue with this program? [Y/n]")
decision = input()
cont = False  # whether the script continues
for str_i in affirmatives:  # technically less efficient but easier to follow
	if decision.lower() == str_i:
		cont = True

# reject anything that isn't in the 'affirmatives' array
if not cont:
	print("Goodbye!")
	exit()

inputs = {  # list of inputs to capture, for efficiency's sake
	'year': ["Please enter a 4 digit year: ", None],  # use None to show our array's structure
	'month': ["Please enter a 2 digit month: ", None],
	'day': ["Please enter a 2 digit day: ", None]
}
months = {
	'January': 31,
	'February': 29,
	'March': 31,
	'April': 30,
	'May': 31,
	'June': 30,
	'July': 31,
	'August': 31,
	'September': 30,
	'October': 31,
	'November': 30,
	'December': 31
}

for v in list(inputs):  # where v represents value
	array = inputs[v]
	question = array[0]  # get preset question
	print(question)
	inp = input()
	inputs[v] = [question, inp]  # update the 'None' in the lists with captured input

# validating input
for i, v in enumerate(list(inputs)):  # where i represents index and v represents value
	inp = inputs[v][1]  # get the input from our dictionary of inputs
	if i == 0:  # make a special case for year, which has to have a length of 4
		assert len(inp) == 4, "Invalid year length!"  # check if year is 4 characters long
		assert int(inp), "Year is not a valid integer!"  # also validate our input
		inputs[v] = [inputs[v][0], int(inp)]
	else:  # if we aren't checking year (iterations other than first)
		assert len(inp) == 2, f"Invalid {i == 1 and 'month' or 'day'} length!"  # both month and day must be 2 chars
		assert int(inp), f"{i == 1 and 'Month' or 'Day'} is not a valid integer!"  # also validate our input
		if i == 1:
			assert int(inp) <= 12, "Month input must be 1-12!"
		elif i == 2:
			assert int(inp) <= months[list(months)[(inputs['month'][1] - 1)]], "Given day exceeds number of days in given month"
		inputs[v] = [inputs[v][0], int(inp)]


def julian(y, m, d):  # make a simplified function for cleaner code
	return d + (153 * m + 2) / 5 + y * 365 + y / 4 - 32045


def concatArray(arr, sep):  # function to simplify formatting array (aka our Gregorian date)
	str1 = ""
	for i, v in enumerate(arr):  # where i represents index and v represents value
		if (i + 1) < len(arr):  # add one to index to account for zero-indexed lists
			str1 = str1 + (len(str(v)) > 1 and str(v) or f"0{str(v)}") + sep  # prefix single digit characters with a 0
		else:
			str1 = str1 + (len(str(v)) > 1 and str(v) or f"0{str(v)}")  # prefix single digit characters with a 0
	return str1


args = []  # just so we don't have an ugly print statement
for obj in list(inputs):  # add all of our arguments to an array for simplicity
	args = [*args, inputs[obj][1]]  # fastest way to append to an array

print(
	f'\n\nYou entered the Gregorian date {concatArray(args, "-")}, which is equivalent to the Julian date {julian(*args)}.')
