# function_exercises

# 1 Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(a): # this is defining the function and adding a variable
    if a == 2: # this is setting the variable equal to 2
        return True #returns the value true if the variable entered is 2
    else:
        False

def is_two(b):
    return (b == 2) or (b == '2') # returns a 2 or string of 2

print(is_two(2)) # returns a True
print(is_two(3)) # returns a None ?
    

# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(a):
    if a == ("a", "e", "i", "o", "u"):
        return True
    else:
        False

print(is_vowel("a")) # returns a none value
print(is_vowel("x"))
# the above function did not work and I believe it is reading as if a == "a" but still returned a none value


def is_vowel(vowel):
    return vowel.lower() in 'aeiou' # using the in function to include all vowels

print(is_vowel("a")) # this one works, returns a True statememt
print(is_vowel("b")) # returns a False statement


# 3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. #
# Use your is_vowel function to accomplish this.
def is_consonant(consonant): #defining the function
    return consonant.lower() in 'bcdfghjklmnpqrstvwxyz' # using the in function to identify consonants

print(is_consonant('x')) # True
print(is_consonant('a')) # False

# example
 def is_consonant(string):
     return string.lower() not in 'aeiou'

string = "I"

is_consonant(string)

# use is_vowel function
string = "t"
is_vowel(string) == False

def is_consonsnt(string):
    return is_vowel(string) == False


# 4 Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_string_is_a_word(word):
    if word[0] not in 'aeiou'
        word = word.capitalize()
    return word

print(capitalize_string_is_a_word(tacos)


# 5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip. 
# tip percentage %5 %10 %20
# bill total
# return amount to tip[]
def calculate_tip(percentage, sub_total):
    tip = ((sub_total * (percentage / 100))
    total = (sub_total + tip)
    return total

sub_total = input("What is the bill total?")

percentage = input("What percent do you want to tip, ex. 10, 15, 20?")

print(calculate tip(percentage, sub_total)) # still a work in progress, not able to get an end total


# 6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.


def apply_discount(original_price, discount_percent):
    

# 7 Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(comma):
    number = ""
    for char in comma:
        if char not in ",":
            number += char
    return float(number)

print(handle_commas(12,34))
print(handle_commas(1,,,,000)) # not sure if this works, need to update

# 8 Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if type(grade) == str:
        return "Not valid number grade"
    elif type(grade) == float or int:
        if grade <= 100 and grade >= 90:
            return "A"
        if grade <= 89 and grade >= 80:
            return "B"
        if grade <= 79 and grade >= 70:
            return "C"
        if grade <= 69 and grade >= 60:
            return "D"
        if grade <= 59:
            return "F"

print(get_letter_grade(90))
print(get_letter_grade(80))
print(get_letter_grade(70))
print(get_letter_grade(60))
print(get_letter_grade(59))



# 9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(something):
    letters = list(something)
    for letter in letters:
        if is_vowel(letter):
            letters.remove(letter)
    return ''.join(letters)

print(remove_vowels("tacos"))
print(remove_vowels("enchiladas"))
print(remove_vowels("nachos"))

# example

def remove_vowels(string):
    no_vowels = ""
    for char in string:
        if char.lower() not in "aeiou":
            no_vowels += char
    return no_vowels

print(remove_vowels("tacos"))
print(remove_vowels("enchiladas"))
print(remove_vowels("nachos"))


# 10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
## anything that is not a valid python identifier should be removed, leading and trailing whitespace should be removed, 
# everything should be lowercase,
# spaces should be replaced with underscores
def normalize_name(name):
        normalized = name.lower()
        
        if normalized.endswith(u"_name"):
            useless_suffix_length = len(u"_name")
            normalized = normalized[:-useless_suffix_length]
        elif normalized.endswith(u"_name;"):
            useless_suffix_length = len(u"_name;")
            normalized = normalized[:-useless_suffix_length]

        if normalized.startswith(u"$"):
            normalized = normalized[1:]

 
        if normalized.startswith((u"int_", u"ext_", u"hpt_")):
            normalized = normalized[4:]
        return normalized 
    
print(normalize_name("NAME"))
print(normalize_name("Name"))
print(normalize_name("FirstName")) # did not return expected result
# still working on solution for this problem

# example
# use this as a test name
# "1 2 3 $()&^$( T#%^H#%^i%^s%^ i%^&S %&(*(a v$%&AlI#%^d p#%^YTh#%^on id#%^%&en$%&TI#$^%%$&^*Fi@$%^*(er  #^#^#@"
# this_is_a_valid_python_identifier



# 11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(number):
    return sum(number)  # this only summed the numbers in the list and did not answer the question

print(cumulative_sum([1,2,3,4,5]))  # 15 summed up the list but not returning a cummulative list
print(cumulative_sum([6,7,8,9,10]))  # this just gave a sum of all the numbers in the list (40)


list = [1,2,3,4] # established a list of numbers
new_list = [] # created a new list
total = 0 # setting a startpoint
for i in range(0,len(list)):
    total += list[i]
    new_list.append(total)
     
print(new_list) # works but with a list input
# [1, 3, 6, 10]


# additional exercise
# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Comment each line of your function with an explanation of what that line is doing. 
# Make sure to document both the type of all function parameters and the type that will be returned from the function. 
# also be sure to use the vocabulary we've introduced to describe your python code appropriately.
# Walk us through how the function executes using the comments you wrote and several different example inputs that demonstrate all the possible paths through your function.

# bonus exercise

# 1 Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

# 2 Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
