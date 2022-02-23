"""
Assignment Problem, Week 3 Question One (Interest Rate)
Author: Raforawesome
Due Date: Feb 25, 2022 11:59 PM
Question or problem: Sem 2 Week 3 Q 1- Interest rate Function
Class: ICS3UI-02
"""


# My function
def calc_p_int(price, rate, tm):
	return (rate != 0 and tm != 0) and (price * (rate / 100) * tm) or price


# DO NOT modify this part, (with only one exception - formatting) - just add comments to show understanding.

while True:
	p = input("Please enter the principal amount you borrowed for your home: ")
	if p.isdigit():  # Checks if the input strings consists of only digits
		p = int(p)
		# now get interest rate
		r = float(input("Please enter the interest rate as a single or double digit: "))
		if type(r) == float:  # check if cast input is actually a float (errors)

			t = input("Please enter the time, in years that you will be paying for your home: ")
			if t.isdigit():  # check if given input only consists of digits
				t = int(t)
				print("Your principal is ${:.2f}".format(p), "at", r, "% for", t, "years")
				print("Borrowing will cost you, ${:.2f}".format(calc_p_int(p, r, t)), end="\n\n")
	else:  # If the input was not an integer, prompt the user to insert an integer again.
		print("Incorrect data has been entered. Please insert an integer, we are beginning again.\n")
