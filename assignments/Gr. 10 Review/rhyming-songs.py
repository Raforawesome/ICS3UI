"""
Assignment Question week 3, question 2
Author: Raforawesome
Due Date: Feb 25, 2022 11:59 PM
Question or problem: Rhyming Songs/lyrics
Class: ICS3UI-02
"""
verses = 10
phonetics = {
	10: 'ten',
	9: 'nine',
	8: 'eight',
	7: 'seven',
	6: 'six',
	5: 'five',
	4: 'four',
	3: 'three',
	2: 'two',
	1: 'one'
}

def get_verse(num):
	return f"""There were {phonetics[num]} in the bed
And the little one said,
“Roll over! Roll over!”
So they all rolled over and
one fell out
"""

for i in range(10, 0, -1):
	print(get_verse(i))
