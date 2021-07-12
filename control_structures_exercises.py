# control_structure_exercises

#1 Conditional Basics

## a. prompt the user for a day of the week, print out whether the day is Monday or not
days_of_the_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
is_it_monday = input(f'What day is today?')
for day in days_of_the_week: 
    if day == 'Monday':
        continue
    print(f'Sounds like somebody has a case of the {day}s')
else:
        print("Today seems like a good day")

## b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
what_day_is_it = input(f"Might I inquire as to what day of the week it is?")
for weekday in what_day_is_it:
    if day == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        print("Today is a Weekday")
else:
    print("Weekend Vibes")

## c. create variables and make up values for

### the number of hours worked in one week

### the hourly rate

### how much the week's paycheck will be


#2 Loop Basics

## a. While

### create an integer variable "i" with a value of 5

### create a loop that runs so long as "i" is less than or equal to 15

### each loop iteration, output the current value of "i", then increment "1" by one

i = 5
while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

i = 2
while i <= 100000:
    print(i)
    i =+ i**2

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


# b. For Loops

## i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

