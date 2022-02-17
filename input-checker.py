"""
Assignment Question 2/1
Author: Raforawesome
Due Date: Feb 17, 2022 11:59 PM
Question or problem: Option B - Input Checker
Class: ICS3UI-02
"""

vowels = ['a', 'e', 'i', 'o', 'u']
affirmatives = ['y', 'yes']
negatives = ['n', 'no']


def run():  # make a function and use recursion to repeat the program
	questions = [  # preset questions to ask, for efficient code
		"Enter a 4-digit whole number: ",
		"Enter an integer less than 50: ",
		"Enter a decimal number: ",
		"Enter a string that begins with a vowel: ",
		"Enter a string that ends with a consonant: "
	]


	for i in range(1, len(questions) + 1):  # add one because range loops are exclusive
		question = questions[i - 1]  # subtract one to account for zero-indexing

		if i == 1:  # 4 digit whole number
			_input = input(question)  # prefix variable with underscore as 'input' is already a global
			check = True  # start off being true
			message = ""  # make our message change depending on what exactly is wrong

			if not len(_input) == 4:  # our input must be 4 digits
				check = False
				message = "Input must be 4 characters!\n"

			if not _input.isnumeric() and check:  # check if our input consists of only numbers
				check = False
				message = "Whole numbers must be integers!\n"
			
			if check and not int(_input) >= 0:  # check if our number is above 0 (no negatives)
				check = False
				message = "Whole numbers must be positive!\n"

			if check:  # if none of those if statements set check to false, send success message
				message = "That works!\n"
			print(message)


		elif i == 2:  # integer below 50
			_input = input(question)  # prefix variable with underscore as 'input' is already a global

			try:  # see if casting input to int errors
				int(_input)
			except:
				print("This number isn't an integer.\n")
			else:
				num = int(_input)

				if num >= 50:
					print("This integer isn't below 50!\n")
				else:
					print("That works!\n")


		elif i == 3:
			_input = input(question)  # prefix variable with underscore as 'input' is already a global
			
			try:
				float(_input)
			except:
				print('Provided input is not a valid decimal number.\n')
			else:
				if not _input.isnumeric():
					print("That works!\n")
				else:
					print("That isn't a decimal number!\n")


		elif i == 4:
			_input = input(question)  # prefix variable with underscore as 'input' is already a global
			char = _input[:1]

			if char.lower() in vowels:
				print("That works!\n")
			else:
				print("The first character of this string is not a vowel!\n")


		elif i == 5:
			_input = input(question)  # prefix variable with underscore as 'input' is already a global
			char = _input[len(_input) - 1:len(_input)]

			if (char.lower() in vowels) == False:
				print("That works!\n")
			else:
				print("The last character of this string is not a consonant!\n")


	rerun = True  # default value doesn't matter
	while True:  # make checking code repeat until a valid answer is given
		_input = input("\nWould you like to repeat the program? [Y/n]  ")
		if _input.lower() in affirmatives:  # if the given answers is on our "yes list"
			rerun = True  # enable rerun flag if they answered yes
			break  # end the infinite loop
		elif _input.lower() in negatives:  # if the given answers is on our "no list"
			rerun = False  # disable the rerun flag since they answered no
			break  # end the infinite loop
		else:
			print('Invalid input!')  # if they didn't answer properly, let them know
			continue  # and continue asking until we get an answer

	if rerun:
		print('\n')  # just for formatting, makes the next line distanced
		run()  # re-run this same function (recursion)
	else:
		exit()

run()