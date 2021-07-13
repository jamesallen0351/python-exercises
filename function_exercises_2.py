# function exercises 2, cleaned up version to to help with imports

#1
def is_two(b):
    return (b == 2) or (b == '2') # returns a 2 or string of 2

#2
def is_vowel(vowel):
    return vowel.lower() in 'aeiou' # using the in function to include all vowels


#3
string = "t"
is_vowel(string) == False

def is_consonsnt(string):
    return is_vowel(string) == False

#4
def capitalize_non_vowel(word):
    if word[0] not in 'aeiou':
        word = word.capitalize()
    return word

#5
bill = 100
tip_percent = 20

def calculate_tip(bill, tip_percent):
    return bill * (tip_percent / 100)

#6
price = 300
discount_percent = 20

def apply_discount(price, discount_percent):
    
    return price - (price * (discount_percent / 100))

#7
def handle_commas(string):
    number = ""
    for char in string:
        if char not in ",":
            number += char
    return float(number)

#8
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

#9
def remove_vowels(something):
    letters = list(something)
    for letter in letters:
        if is_vowel(letter):
            letters.remove(letter)
    return ''.join(letters)



#10

#11
list = [1,2,3,4] # established a list of numbers
new_list = [] # created a new list
total = 0 # setting a startpoint
for i in range(0,len(list)):
    total += list[i]
    new_list.append(total)
     