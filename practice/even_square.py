def is_an_even_square(number):


# Don't modify this part
while True:
	num = int(input("Enter an integer: "))

	if is_an_even_square(num):
		print(num, "is an even square number.", end="\n\n")
	elif is_an_even_square(num) is None:
		print("It cannot be determined whether", num, "is an even square number.", end="\n\n")
	else:
		print(num, "is NOT an even square number.", end="\n\n")