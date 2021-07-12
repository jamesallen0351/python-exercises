# 17 list comprehension exercises

# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [f.upper() for f in fruits]

print("Exercise 1 uppercased fruits", uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [f.capitalize() for f in fruits]

print("Exercise 2 capitalized fruits", capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if [fruit, len([x for x in fruit if x in 'aeiou'])][1] >= 2]

print("Exercise 3 fruits with more than 2 vowels", fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if [fruit, len([x for x in fruit if x in 'aeiou'])][1] == 2]

print("Exercise 4 fruits wiht only two vowels", fruits_with_only_two_vowels)
# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_5_characters = [fruit for fruit in fruits if len(fruit) > 5]

print("Exercise 5 fruit with more than 5 characters", more_than_5_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruit_with_5_characters = [fruit for fruit in fruits if len(fruit) == 5]

print("Exercise 6 fruit with exactly 5 characters", fruit_with_5_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_less_than_5_characters =[fruit for fruit in fruits if len(fruit) < 5]

print("Exercise 7 fruit with less than 5 characters", fruits_less_than_5_characters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruits_number_of_characters = [len(fruit) for fruit in fruits]

print("Exersice 8 list of fruits number of characters", fruits_number_of_characters)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits for letter in fruit if letter == "a"]

print("Exercise 9 fruits with letter a", fruits_with_letter_a)
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0 ]

print("Exercise 10 even numbers", even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 == 1]

print("Exercise 11 odd numbers", odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positve_numbers = [number for number in numbers if number >= 0]

print("Exercise 12 positive numbers", positve_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]

print("Exercise 13 negative numbers", negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more_numerals = [number for number in numbers if len(str(number).replace('-', '')) >= 2]

print("Exercise 14 two or more numerals", two_or_more_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number ** 2 for number in numbers]

print("Exercise 15 numbers squared", numbers_squared)
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 == 1 and number < 0]

print("Exercise 16 odd negative numbers", odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]

print("Exercise 15 numbers plus 5", numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes = []