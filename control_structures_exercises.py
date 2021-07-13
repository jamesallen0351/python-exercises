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
# example code
day = input("What day of the week is it?   ")

if day.lower() == "monday":
    print("Today is monday")
else:
    print("Today is not monday")

## b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
what_day_is_it = input(f"Might I inquire as to what day of the week it is?")
for weekday in what_day_is_it:
    if day == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        print("Today is a Weekday")
else:
    print("Weekend Vibes")  #did not work as intended

# adding review notes
print("What day of the week is it?")
day = input()

if day.lower() in ("monday", "tuseday", "wednesday", "thursday", "friday"):  
    print()
    print("Today is a weekday!")  
elif day.lower() in ("saturday", "sunday"):    
    print()
    print("Today is a weekend!") 
else:  
    print()
    print(f"{day} is not a day of the week!")

  



## c. create variables and make up values for

### the number of hours worked in one week
number_of_hours_worked = 40
### the hourly rate
hourly_rate = 20
### how much the week's paycheck will be
paycheck = number_of_hours_worked * hourly_rate

print("This week's paycheck will be", paycheck)

# overtime is time and a half pay
overtime

# example notes
hours_this_week = 50
hourly_rate = 20

# if no overtime, pay = hours_this_week * hourly_rate

# if overtime, pay = (40 * hourly_rate) + overtime

# overtime = (hours_this_week - 40) * (hourly_rate * 1.5)

if hours_this_week <= 40: 
    pay = hours_this_week * hourly_rate 
if hours_this_week > 40:
    overtime = (hours_this_week - 40) * (hourly_rate * 1.5)
    pay = (40 * hourly_rate) + overtime
print(f"Total Wages: {pay}")


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
while i < 100000:
    print(i)
    i =+ i**2

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


# b. For Loops

## i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# prompt user for a number
print("Give me a number!")
input_number = input()
# loop through the list of table numbers
# for each generate a table equation and print results

for tab_num in range(1,11): 
    print(f"{input_number} X {tab_num} = {input_number * tab_num}") # input numbers are interpreted as strings
    # loop through the list of table numbers
# for each generate a table equation and print results

for tab_num in range(1,11):
    
    print(f"{input_number} X {tab_num} = {int(input_number) * tab_num}") # Fix data types by wrapping in desired type


# c. break and continue: Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input.


# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number


# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1


# for loops all together example

while True:
    
    # prompt user for a number
    print("Enter a whole odd number between 1 and 50")
    pick = input()
    
    # check is a number
    if pick.isnumeric() == False:        
        
        print()
        print("Please enter a WHOLE NUMBER!")
        print()
        
        continue
        
    else:
        
        pick = int(pick) # make ready to evaluate as a number
    
    
    # check is an appropriate number
    if (pick > 0) and (pick <51) and (pick %2 != 0):
        
        print()
        print(f"Thank you! Your number is: {pick}")
        print()
        
        break
        
    else:
        
        print()
        print("This number is invalid!")
        print()
        
# print odd number message and yikes message for numbers 1 to 50    
for number in range(1,50):
    
    if number %2 == 0:
        
        continue
        
    if number == pick:
        
        print("Yikes! Skipping number:", number)
        
        continue
        
    print("Here is an odd number:", number)

# 3 Fizzbuzz

## Write a program that prints the numbers from 1 to 100
i = 0
while i <= 100:
    print(i)
    i += 1
## For multiples of three print "Fizz" instead of the number
## For the multiples of five print "Buzz".
## For numbers which are multiples of both three and five print "FizzBuzz"
for r in range(1, 101):
    if r % 15 == 0:  # multiples of 15 contain 3 and 5 and need both fizz and buzz, first on loop check
        print("FizzBuzz")
    elif r % 3 == 0:
        print("Fizz")
    elif r % 5 == 0:
        print("Buzz")
    else:
        print(r)


### alternate fizzbuzz solution    
for fizzbuzz in range(1, 100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)




# 4 Display a table of powers.
## Prompt the user to enter an integer.
## Display a table of squares and cubes from 1 to the value entered.
## Ask if the user wants to continue.
## Assume that the user will enter valid data.
## Only continue if the user agrees to.
# all together now

first = True

while True:
    
    # if this is the first time through the loop go right to table prompt
    if first == True:
        
        first = False
        
        persist = 'y'
        
    # if this is not the first time through the loop prompt user to continue
    else:
      
        print("Do you wish to continue? (y/n)")
        persist = input()
        print()

        
    # Display table prompt / Quit / Re-prompt
    if persist.lower() == 'y':

        # prompt user for positive whole number
        while True:
    
            # prompt user for a number
            print("Enter a positive whole number!")
            pick = input()

            # check is a number
            if pick.isnumeric() == False:        

                print()
                print("Please enter a POSITIVE WHOLE NUMBER!")
                print()
                
            else:
        
                pick = int(pick) 
            
                break
                
                
        # print titles
        print() # adding space
        print(" Number |Squared |Cubed  ")
        print("|-------|--------|-----|")

        # print body of chart
        for r in range(1,pick+1):

            print("|{:<7}|{:<8}|{:<5}|".format(r,r**2,r**3))

        
        print() # adding space
        
    elif persist.lower() == 'n':

        break

    else:

        continue



# 5 Convert given number grades into letter grades.

## Prompt the user for a numerical grade from 0 to 100.
## Display the corresponding letter grade.
## Prompt the user to continue.
## Assume that the user will enter valid integers for the grades.
## The application should only continue if the user agrees to.
## Grade Ranges:A : 100 - 88, B : 87 - 80, C : 79 - 67, D : 66 - 60, F : 59 - 0
### bonus Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+)

wants_to_continue = True
while wants_to_continue:
    grade = int(input('Input a grade from 0 to 100:\n'))
    if grade >= 95:
        print('A+')
    elif grade >= 90:
        print('A')
    elif grade >= 88:
        print('A-')
    elif grade >= 85:
        print('B+')
    elif grade >= 83:
        print('B')
    elif grade >= 80:
        print('B-')
    elif grade >= 75:
        print('C+')
    elif grade >= 70:
        print('C')
    elif grade >= 67:
        print('C-')    
    elif grade >= 64:
        print('D+')
    elif grade >= 62:
        print('D')
    elif grade >= 60:
        print('D-')
    else:
        print('F')
    if input('Do you want to stop?\n').lower() in ('y', 'yes'):
        wants_to_continue = False

# 6 Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre.
## Loop through the list and print out information about each book.
## Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.