# Part -2 Python Basics (Conditional Statements)
# 1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
#Type your code here
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = salary * 0.05  
    print("Your bonus amount is:", bonus)
else:
    print("No bonus awarded.")

print("------------------------------------------------")


# 2) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
#Type your code here
age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")

print("------------------------------------------------")

# 3) Write a program to check whether a number entered by user is even or odd.
#Type your code here
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("------------------------------------------------")

# 4) Write a program to check whether a number is divisible by 7 or not.
# Show Answer
#Type your code here
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")

print("------------------------------------------------")

# 5) Write a program to display 
# "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
#Type your code here
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

print("------------------------------------------------")

# 7) Write a program to display the last digit of a number.

#Type your code here
num = int(input("Enter a number: "))

last_digit = num % 10

print("The last digit is:", last_digit)

print("------------------------------------------------")

# 9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
#Type your code here 
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")

print("------------------------------------------------")

# 10) Take two int values from user and print greatest among them.
# Type your code here
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The greatest number is:", num1)
elif num2 > num1:
    print("The greatest number is:", num2)
else:
    print("Both numbers are equal.")

print("------------------------------------------------")

# 11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
#Type your code here
quantity = int(input("Enter the quantity: "))

cost = quantity * 100  

if cost > 1000:
    discount = cost * 0.10  
    total_cost = cost - discount
else:
    total_cost = cost

print("Total cost:", total_cost)

print("------------------------------------------------")

# 12) A school has following rules for grading system:

# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade.
#Type your code here
marks = int(input("Enter your marks: "))

if marks < 25:
    print("Grade: F")
elif marks < 45:
    print("Grade: E")
elif marks < 50:
    print("Grade: D")
elif marks < 60:
    print("Grade: C")
elif marks < 80:
    print("Grade: B")
else:
    print("Grade: A")

print("------------------------------------------------")

# 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# Take following input from user

# - Number of classes held

# - Number of classes attended.

# And print

# - percentage of class attended

# - Is student is allowed to sit in exam or not.

#Type your code here
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print("Attendance Percentage:", attendance_percentage, "%")

if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is NOT allowed to sit in the exam.")

print("------------------------------------------------")

# 15) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
#Type your code here
attendance = int(input("Enter your attendance percentage: "))

if attendance >= 75:
    print("You are allowed to sit for the exam.")
else:
    medical_cause = input("Do you have a medical cause? (Y/N): ")
    if medical_cause == 'Y':
        print("You are allowed to sit for the exam due to medical reasons.")
    else:
        print("You are not allowed to sit for the exam.")

print("------------------------------------------------")

# 16) Write a program to check if a year is leap year or not.

# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
# #Type your code here
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

print("------------------------------------------------")

# 17) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR"
#Type your code here
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
marital_status = input("Enter your marital status (Y/N): ")

if gender == 'F':
    print("You will work only in urban areas.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("You may work anywhere.")
    elif 40 < age <= 60:
        print("You will work only in urban areas.")
    else:
        print("ERROR")
else:
    print("Invalid input for gender.")

print("------------------------------------------------")

# 6) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#      Unit                                                     Price  
# uptp 100 units                                             no charge
# Next 200 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs.3500
# (For example if input unit is 97 than total bill amount is Rs.0
# (For example if input unit is 150 than total bill amount is Rs.750
# 13) Take input of age of 3 people by user and determine oldest and youngest among them.
#Type your code here
units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10

print("Total bill amount is Rs.", bill)
