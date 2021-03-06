# This program builds a dictionary for ICS3UI
import csv
import sys

# set up variables required throughout
global choice

# this would have been so much easier if I'd taught you I/O first!
jobs = {
	"College Agriculture natural resources and conservation Closely related": "941",
	"College Agriculture natural resources and conservation Somewhat related": "320",
	"College Agriculture natural resources and conservation Not related at all": "373",
	"College Agriculture natural resources and conservation Total": "1634",
	"College Computer science mathematics and statistics Closely related": "1880",
	"College Computer science mathematics and statistics Somewhat related": "530",
	"College Computer science mathematics and statistics Not related at all": "511",
	"College Computer science mathematics and statistics Total": "2921",
	"College Education Closely related": "2020",
	"College Education Somewhat related": "364",
	"College Education Not related at all": "334",
	"College Education Total": "2718",
	"College Architecture and engineering Closely related": "993",
	"College Architecture and engineering Somewhat related": "0",
	"College Architecture and engineering Not related at all": "0",
	"College Architecture and engineering Total": "1588",
	"College Physical and life sciences technologies Closely related": "489",
	"College Physical and life sciences technologies Somewhat related": "0",
	"College Physical and life sciences technologies Not related at all": "0",
	"College Physical and life sciences technologies Total": "713",
	"College Humanities Closely related": "622",
	"College Humanities Somewhat related": "423",
	"College Humanities Not related at all": "1391",
	"College Humanities Total": "2437",
	"College Social and behavioural sciences Closely related": "6897",
	"College Social and behavioural sciences Somewhat related": "2096",
	"College Social and behavioural sciences Not related at all": "2451",
	"College Social and behavioural sciences Total": "11444",
	"College Design music performing fine and applied arts Closely related": "1100",
	"College Design music performing fine and applied arts Somewhat related": "707",
	"College Design music performing fine and applied arts Not related at all": "1541",
	"College Design music performing fine and applied arts Total": "3347",
	"College Health parks recreation and fitness Closely related": "17164",
	"College Health parks recreation and fitness Somewhat related": "1645",
	"College Health parks recreation and fitness Not related at all": "3033",
	"College Health parks recreation and fitness Total": "21842",
	"College Business management marketing and related support services Closely related": "15451",
	"College Business management marketing and related support services Somewhat related": "8773",
	"College Business management marketing and related support services Not related at all": "7190",
	"College Business management marketing and related support services Total": "31414",
	"College Trades and engineering technologies/technicians Closely related": "12814",
	"College Trades and engineering technologies/technicians Somewhat related": "3680",
	"College Trades and engineering technologies/technicians Not related at all": "3603",
	"College Trades and engineering technologies/technicians  Total": "20098",
	"College Personal and culinary services and transportation Closely related": "2585",
	"College Personal and culinary services and transportation Somewhat related": "551",
	"College Personal and culinary services and transportation Not related at all": "856",
	"College Personal and culinary services and transportation Total": "3992",
	"University Agriculture natural resources and conservation Closely related": "679",
	"University Agriculture natural resources and conservation Somewhat related": "371",
	"University Agriculture natural resources and conservation Not related at all": "186",
	"University Agriculture natural resources and conservation Total": "1236",
	"University Computer science mathematics and statistics Closely related": "1362",
	"University Computer science mathematics and statistics Somewhat related": "630",
	"University Computer science mathematics and statistics Not related at all": "319",
	"University Computer science mathematics and statistics Total": "2311",
	"University Education Closely related": "11312",
	"University Education Somewhat related": "1325",
	"University Education Not related at all": "2120",
	"University Education Total": "14757",
	"University Architecture and engineering Closely related": "6325",
	"University Architecture and engineering Somewhat related": "0",
	"University Architecture and engineering Not related at all": "0",
	"University Architecture and engineering Total": "9323",
	"University Physical and life sciences technologies Closely related": "2702",
	"University Physical and life sciences technologies Somewhat related": "2411",
	"University Physical and life sciences technologies Not related at all": "3522",
	"University Physical and life sciences technologies Total": "8635",
	"University Humanities Closely related": "4806",
	"University Humanities Somewhat related": "4622",
	"University Humanities Not related at all": "6937",
	"University Humanities Total": "16365",
	"University Social and behavioural sciences Closely related": "11148",
	"University Social and behavioural sciences Somewhat related": "7839",
	"University Social and behavioural sciences Not related at all": "8799",
	"University Social and behavioural sciences Total": "27786",
	"University Design music performing fine and applied arts Closely related": "1502",
	"University Design music performing fine and applied arts Somewhat related": "1052",
	"University Design music performing fine and applied arts Not related at all": "1976",
	"University Design music performing fine and applied arts Total": "4529",
	"University Health parks recreation and fitness Closely related": "13745",
	"University Health parks recreation and fitness Somewhat related": "1749",
	"University Health parks recreation and fitness Not related at all": "1870",
	"University Health parks recreation and fitness Total": "17365",
	"University Business management marketing and related support services Closely related": "16352",
	"University Business management marketing and related support services Somewhat related": "7981",
	"University Business management marketing and related support services Not related at all": "2913",
	"University Business management marketing and related support services Total": "27246",
	"Masters Agriculture natural resources and conservation Closely related": "404",
	"Masters Agriculture natural resources and conservation Somewhat related": "209",
	"Masters Agriculture natural resources and conservation Not related at all": "85",
	"Masters Agriculture natural resources and conservation Total": "698",
	"Masters Computer science mathematics and statistics Closely related": "829",
	"Masters Computer science mathematics and statistics Somewhat related": "357",
	"Masters Computer science mathematics and statistics Not related at all": "51",
	"Masters Computer science mathematics and statistics Total": "1238",
	"Masters Education Closely related": "3115",
	"Masters Education Somewhat related": "629",
	"Masters Education Not related at all": "125",
	"Masters Education Total": "3869",
	"Masters Architecture and engineering  Closely related": "1879",
	"Masters Architecture and engineering  Somewhat related": "587",
	"Masters Architecture and engineering  Not related at all": "152",
	"Masters Architecture and engineering  Total": "2618",
	"Masters Physical and life sciences technologies Closely related": "1008",
	"Masters Physical and life sciences technologies Somewhat related": "612",
	"Masters Physical and life sciences technologies Not related at all": "239",
	"Masters Physical and life sciences technologies Total": "1859",
	"Masters Humanities Closely related": "705",
	"Masters Humanities Somewhat related": "445",
	"Masters Humanities Not related at all": "346",
	"Masters Humanities Total": "1497",
	"Masters Social and behavioural sciences Closely related": "2295",
	"Masters Social and behavioural sciences Somewhat related": "935",
	"Masters Social and behavioural sciences Not related at all": "507",
	"Masters Social and behavioural sciences Total": "3737",
	"Masters Design  music performing  fine and applied arts Closely related": "216",
	"Masters Design  music performing  fine and applied arts  Somewhat related": "221",
	"Masters Design  music performing  fine and applied arts Not related at all": "85",
	"Masters Design  music performing  fine and applied arts Total": "521"}


# Note: You may not simply add week 4 data given to the list above.
# On your final run, so it is saved in the file, add all degrees.


def lookup():
	# look up a word from week 1 and 2 to check...
	word = input("Please enter one of the jobs- degree: ")
	while word != "":
		print(word, "has", jobs[word], "with jobs in the field.")  # returns value
		word = input("Please enter one of the jobs- degree, press enter to quit: ")
	print("Thank you for using the dictionary of degrees and jobs.")


def add_degree(job, num):
	jobs[job] = num
	print(f"added {job} with {num} degree-jobs")


def remove_degree():
	to_remove = input("Please enter a degree to remove: ")

	if to_remove in jobs.keys():
		del jobs[to_remove]
		print(f"Removed {to_remove} from our database.")

		def recursive_input_1():
			print_key_list = input("Do you want a list of keys?  [Y/n] ")
			if print_key_list == "Y":
				print(jobs.keys())
			elif print_key_list == "n":
				print('\n')
			else:
				print("Invalid input!")
				recursive_input_1()
		recursive_input_1()

	else:
		print("This degree doesn't exist in our database!")

	print("added -in remove - to eliminate hidden characters")  # remove this!


def lookup_no_input(arg):
	return arg in jobs.keys() is not None and True or False


def add_new():
	# check first to be sure word is not already in the dictionary
	check = input("Please add a new degree: ")
	if lookup_no_input(check):  # you will need to change this...
		print("That degree is already in the dictionary")
		return
	else:
		# add the new word and its meaning - your code
		def recursive_input():
			jobs_with_degree = input("Please enter one of the jobs- degree: ")

			if jobs_with_degree.isnumeric():
				jobs[check] = int(jobs_with_degree)
			else:
				print("Please enter a valid number!")
				recursive_input()
		recursive_input()


def key_there():
	inp = input("Please enter the degree: ")
	if inp in jobs.keys():
		print(f"This program {inp} exists in the dictionary.")
	else:
		print(f"{inp} was not found in the dictionary.")


def save_file():
	# fully functional, without error checking - leave alone
	# prompt user for output file where name is the pseudo name or name
	filename = "jobswk3_" + input("please enter your name/pseudo name for the output file: ") + ".txt"
	outfile = open(filename, 'w')
	outfile.write(str(jobs))
	# option, nicer csv, but not yet...
	outfile.close()


def quit_program():
	# fully functional, leave alone
	sys.exit("Bye. Hope you were successful.")


# here's the main program, fully functional, leave alone...
while True:
	print("This program will assist you with some typical Dictionary functions...\n")
	print(" 1. look up a degree")
	print(" 2. remove a degree")
	print(" 3. add the last 8 degree job pairs")
	print(" 4. check to see if the key is already in the dictionary")
	print(" 5. Save your work and Ms. Harris to a csv or txt file.")
	print(" 6. Quit")
	option = int(input(" please enter a menu item number: "))
	if option == 1:
		lookup()
	elif option == 2:
		remove_degree()
	elif option == 3:
		add_new()
	elif option == 4:
		key_there()
	elif option == 5:
		save_file()
	elif option == 6:
		quit_program()
	else:
		# possible invalid entry - check input.
		print("Something went wrong with your option choice, trying again.")
