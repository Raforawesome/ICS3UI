# Make 6 sets
# 1. Make a set of numbers from 1-1000 that are divisible by 3
# 2. Make a set of numbers from 1-1000 that are divisible by 7
# 3. Make a set of numbers from 1-1000 that are divisible by 11
# 4. Make a set of numbers from 1-1000 that are divisible by 3, 7 and 11
# 5. Make a set of numbers from 1-1000 that are divisible by 3 and 7 but not 11
# 6. Make a set of numbers from 1-1000 that are divisible by 3, 7 or 11

list_1 = [x for x in range(1, 1001) if x % 3 == 0]
list_2 = [x for x in range(1, 1001) if x % 7 == 0]
list_3 = [x for x in range(1, 1001) if x % 11 == 0]
list_4 = [x for x in range(1, 1001) if x % 3 == 0 and x % 7 == 0 and x % 11 == 0]
list_5 = [x for x in range(1, 1001) if x % 3 == 0 and x % 7 == 0 and x % 11 != 0]
list_6 = [x for x in range(1, 1001) if x % 3 == 0 or x % 7 == 0 or x % 11 == 0]