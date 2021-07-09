# control_structure_exercises

# Conditional Basics
## a. prompt the user for a day of the week, print out whether the day is Monday or not
days_of_the_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
is_it_monday = input(f'What day is today?')
for day in days_of_the_week: 
    if day == 'Monday':
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


