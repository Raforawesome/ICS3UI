# this is the python function file for Practice 3 week 2
# this file contains a dice function that stops if a 1 is rolled. It then
# returns a total of zero - the person lost!
# If not a 1, the function allows for rolls up to the number of times
# requested for a total number of the dice rolls.
# NOTE:
# With a very small modification (IE: a Yatzee game, this function could be
# easily used for the total of 5 dice.

# we have not yet used the random function in class, but we are about to
# to use the random function, we need to import it.

import random


# now our function

def dice_6sides(times):
	# set up total first
	total = 0
	for i in range(times):  # times is the number of rolls
		die = random.randint(1, 6)
		print(die)  # this can be commented out, but here now for testing purposes
		if die == 1:
			return 0  # game over, no score!  LOST
		else:
			total += die
	return total  # never rolled a one - good score, maybe (all 2s is possible)
