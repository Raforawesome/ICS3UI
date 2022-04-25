# This program builds a dictionary for ICS3UI
import csv
import sys
from parse import parse_file
from fmt import dict_to_JSON

# set up variables required throughout
global choice

# this would have been so much easier if I'd taught you I/O first!
def_temp = parse_file("wk8ReadIn.txt")  # use parse_file to read in the file
definitions = {}  # create an empty dictionary
for k, v in def_temp.items():  # lower all keys to use case-insensitive inputs
	definitions[k.lower()] = v  # add the key and value to the dictionary


def lookup():
	word = input("Please enter one of the definition keys: ").lower()
	while word != "":
		try:
			print(word + ":" + f" {definitions[word]}")  # returns value
		except KeyError:
			print("That word is not in the dictionary.")
		word = input("Please enter a word, press enter to quit: ").lower()
	print("Thank you for using the dictionary of definitions.")


def lookup_no_input(arg):
	return arg in definitions.keys() is not None and True or False


def add_new():
	# check first to be sure word is not already in the dictionary
	check = input("Please add a new definition: ")
	if lookup_no_input(check):  # you will need to change this...
		print("That definition is already in the dictionary")
		return
	else:
		# add the new word and its meaning - your code
		def recursive_input():
			definitions_with_definition = input("Please enter a definition: ")

			if definitions_with_definition.isnumeric():
				definitions[check] = int(definitions_with_definition)
			else:
				print("Please enter a valid number!")
				recursive_input()
		recursive_input()


def key_there():
	inp = input("Please enter the definition: ")
	if inp in definitions.keys():
		print(f"This definition {inp} exists in the dictionary.")
	else:
		print(f"{inp} was not found in the dictionary.")


def save_file():
	# fully functional, without error checking - leave alone
	# prompt user for output file where name is the pseudo name or name
	pn: str = input("please enter your name/pseudo name for the output file: ")
	filename = "definitionswk8_" + pn + ".txt"
	filename2 = "definitionswk8_" + pn + ".json"
	try:
		file = open(filename, "w")
	except OSError:
		print("Could not open file for writing")
		return
	with file:
		file.write(str(definitions))

	try:
		file2 = open(filename2, "w")
	except OSError:
		print("Could not open file for writing")
		return
	with file2:
		file2.write(dict_to_JSON(definitions))


def quit_program():
	# fully functional, leave alone
	sys.exit("Bye. Hope you were successful.")


new_defs = {
	"assert": "enables you to verify if a certain condition is met and throw an exception if it isn’t.",
	"assertion": "a declarative sentence that is either True or False.",
	"defensive programming": "is the process by which you create code that does not crash even when the user might enter something wrong or questionable. Raising an exception is an example of Defensive Programming sometimes referred to as “bullet proofing your code.",
	"else (with reference to a try block)": "lets you code sections that should run only when no exceptions are encountered in the try clause.",
	"Error (Exception)": "incorrect logic in running a program, causing the interpreter to halt.",
	"except": "is used to catch and handle the exception(s) that are encountered in the try clause.",
	"finally": "enables you to execute sections of code that should always run, with or without any previously encountered exceptions.",
	"Handling (or Catching) and Exception": "writing code that specifies what you want to do when an exception occurs. Handling an exception keeps the interpreter from halting when an exception is raised.",
	"Raise": "to generate an exception for example a TypeError, or SyntaxError, or NameError in a program. Also, allows you to throw an error at any time.",
	"Robust": "the ability of a program to execute even when presented with illegal data.",
	"Try": "allows you to “try” a block of code and see if it works, a clause, all statements are executed until an exception is encountered."
}
for k, v in new_defs.items():
	definitions[k] = v


# here's the main program, fully functional, leave alone...
while True:
	print("This program will assist you with some typical Dictionary functions...\n")
	print(" 1. look up a definition")
	print(" 2. check to see if the key is already in the dictionary")
	print(" 3. Save as a dictionary and JSON file.")
	print(" 4. Quit")
	option = int(input(" please enter a menu item number: "))
	if option == 1:
		lookup()
	elif option == 2:
		key_there()
	elif option == 3:
		save_file()
	elif option == 4:
		quit_program()
	else:
		# possible invalid entry - check input.
		print("Something went wrong with your option choice, trying again.")
