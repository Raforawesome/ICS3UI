"""
Practice Problem, Week 10
Author: Raforawesome
Due Date: Apr 30, 2022 11:59 PM
Question or problem: Wk 10 Question 1
Class: ICS3UI-02
"""
'''*** Watch for my comments with *******
***    - big hints for what you need to add -also where you need to add it.
*** Note: There are pieces of code you should not touch shown with ~~~~ in the comments
'''

from datetime import date


class Student:
	name = ""
	surname = ""
	age = ""
	num = ""

	def __init__(self, name, surname, age, num):
		# **** Add code here hint, every line starts with 'self.'
		self.name, self.surname, self.age, self.num = name, surname, age, num

	# ~~~~ do not touch this, helpful for your testing - it works!
	def prnt_details(self, name, surname, age, num):
		return f'Student Name: {name}\nStudent Last Name: {surname}\nStudent Number: {num}\nCurrent Age: {age}'

	# ~~~~ do not touch this! it works, you will need to format what comes back.
	def calculate_age(self, name, birth_year):
		# calculate age and set it as an age
		# return new object
		return f'{name}\t {date.today().year - birth_year}'

	def show(self):
		pass

	# ******print(.....
	'''This was used to print out very basic test cases - see show below
	in the program - check to see it was working before all functionality'''


class School:  # ~~~~~~~~ given - it works! Don't toudh this.
	def __init__(self, *subjects):
		self.subjects = list(subjects)

	def prnt_subjects(self, *subjects):
		pass
	# ******** need to add code here to get printout and/or save to list
	# Hint: return ...
	# 2nd Hint - see prnt_details


class Subject:
	def __add__(self, other):
		pass
	# *********** need to add code here to get printout and/or save to list
	# Hint: return...


def ask_first():
	try:
		first = input("Please enter the student's first name: ")
	except EOFError as E:  # Thrown when input() hits EOF without inpu
		print("Something went wrong!")
	else:
		return first
		print("Checking, remove first", first)  # only happens if return is not successful


def ask_last():
	pass


# ********** Very similar to ask_first you COULD combine


def ask_cur_age():
	try:
		know_age = input("Do you know the student's current age? (y/n)")
		if know_age.lower() == 'n':
			# ask the year they were born
			year = input("Please enter the year the student was born (yyyy): ")
			# call the class to calculate the age
			cur_age = Student.calculate_age("calc", "Name", year)
		# *********** Note how this returns, you might want to strip?
		# cur_age = ___________
		else:
			# user input the age
			cur_age = input("Please enter the student's current age: ")
	except:
		pass


# *********** similar to above returning the values you need or appropriate response

def ask_st_num():
	try:
		st_num = input("Please enter the student's student number: ")
	except:
		pass


# ****** finish this off

def ask_subj1():
	try:
		subj1 = input("Please enter the student's first Subject for this semester: ")
	except:
		pass


# ********* finish this off
def ask_subj2():
	try:
		pass
	except:
		pass


# ********* finish this off or incorporate it into subj1 for each subject

def ask_subj3():
	try:
		pass
	except:
		pass


# ********* finish this off or incorporate it into subj1 for each subject

def ask_subj4():
	try:
		pass
	except:
		pass


# ********* finish this off or incorporate it into subj1 for each subject


keep_running = True
while keep_running == True:
	quit = input("Would you like to enter another student's information (y/n): ")
	if quit.lower() == 'n':
		keep_running = False
		print("Student entry exiting.")
	else:
		# get the date you need - could improve this
		first = ask_first()
		last = ask_last()
		cur_age = ask_cur_age()
		st_num = ask_st_num()
		subj1 = ask_subj1()
		subj2 = ask_subj2()
		subj3 = ask_subj3()
		subj4 = ask_subj4()
	'''~~~~~~~~~~
	This line will work, before you've added everything and 
	just the class has been written properly - left this line in for your
	benefit.  Feel free to uncomment and recomment as you test.
	x = Student.prnt_details('studentRec',"Ali", "Anderson", 20, 987654321) #
	'''
	print("Here is the information captured for this student at WCI:")
	x = Student.prnt_details('studentRec', first, last, cur_age, st_num)
	print(x)
	'''~~~~~~~~~~
	This line, y, will work, before you've added everything and 
	just the class has been written properly - left this line in for your
	benefit.  Feel free ot uncomment and recomment as you test.
	y = School.prnt_subjects('WCI','ICS3UI', "MCR3UI", 'END3UI','TEJ3MI')
	'''
	y = School.prnt_subjects('WCI', subj1, subj2, subj3, subj4)
	print(y)
	print()  # want spacing as you see in the output

	# ~~~~~~~~the next lines work for testing when you have only written the Class
	'''
	jessica = Student('Jessica','Jones', 20,54321)
	jessica.show()

	# create new object using the factory method
	joy = Student.calculate_age("Joy","Joy", 1995)
	print(joy)
	'''
