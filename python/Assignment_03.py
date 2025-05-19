# 1. Write a program that accepts a string from user. Your program should count and display number of 
# vowels in that string.
string = input("Enter a string: ")
count = 0

for char in string:
    if char in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)
 
#  2. Write a program that reads a string from keyboard and display: 
# * The number of uppercase letters in the string 
# * The number of lowercase letters in the string 
# * The number of digits in the string 
# * The number of whitespace characters in the string


string = input("Enter a string: ")

upper = 0
lower = 0
digits = 0
spaces = 0

for char in string:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Whitespace characters:", spaces)
 
# 3. Write a Python program that accepts a string from user. Your program should create and display a 
# new string where the first and last characters have been exchanged. 
# For example if the user enters the string 'HELLO' then new string would be 'OELLH' 

string = input("Enter a string: ")

if len(string) > 1:
    new_string = string[-1] + string[1:-1] + string[0]
else:
    new_string = string  

print("New string:", new_string)

# 4. Write a Python program that accepts a string from user. Your program should create a new string in 
# reverse of first string and display it. 
# For example if the user enters the string 'EXAM' then new string would be 'MAXE'  

string = input("Enter a string: ")
new_string = string[::-1]  
print("Reversed string:", new_string)

# 5. Write a Python program that accepts a string from user. Your program should create a new string by 
# shifting one position to left. 
# For example if the user enters the string 'examination 2021' then new string would be 'xamination 
# 2021e'  

string = input("Enter a string: ")

if len(string) > 1:
    new_string = string[1:] + string[0]  
else:
    new_string = string 

print("New string:", new_string)

# 6. Write a program that asks the user to input his name and print its initials. Assuming that the user 
# always types first name, middle name and last name and does not include any unnecessary spaces. 
# For example, if the user enters Ajay Kumar Garg the program should display A. K. G. 
# Note:Don't use split() method 

name = input("Enter your full name: ")

initials = name[0] + ". "  

for i in range(1, len(name)):
    if name[i] == " ":  
        initials += name[i + 1] + ". "  

print("Initials:", initials.strip())

# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad, 
# madam and radar are all palindromes. Write a programs that determines whether the string is a 
# palindrome. 
# Note: do not use reverse() method 

string = input("Enter a string: ")

# Compare the string with its reverse using slicing
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 8. Write a program that display following output: 
# SHIFT 
# HIFTS 
# IFTSH 
# FTSHI 
# TSHIF 
# SHIFT  
    
word = "SHIFT"

for i in range(len(word)):  
    shifted_word = word[i:] + word[:i]  
    print(shifted_word)

print(word)  


# 9. Write a program in python that accepts a string to setup a passwords. Your entered password must 
# meet the following requirements: 
# The password must be at least eight characters long. 
# It must contain at least one uppercase letter. 
# It must contain at least one lowercase letter. 
# It must contain at least one numeric digit. 
# Your program should should perform this validation.  

password = input("Enter a password: ")


has_upper = False
has_lower = False
has_digit = False

# Check length
if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

# Final validation
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Password is valid!")
else:
    print("Invalid password! It must be at least 8 characters long, contain an uppercase letter, a lowercase letter, and a digit.")