# Part -1 Python Basics (Variables)
# 1. Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
# Write your code here
print("Name:Moeez Ahmed Khan\nFather's Name:Khalid Ahmed Khan\nDate of Birth:02-08-2004")

print("------------------------------------------------")

# 2. Write your small bio using variables and print it using print function
# Write your code here
name = "Moeez Ahmed Khan"
father_name = "Khalid Ahmed Khan"
dob = "02-08-2004"
education = "BSCS in Virtual University"
skills = "Web Development, UI/UX Design, PHP, Laravel, Angular, C#, ASP.NET"
experience = "Worked on Hospital Management System, E-commerce Website, Lawyer Management System"
goal = "Specializing in Full Stack Development for Mobile & Desktop Applications"


print("----- My Bio -----")
print(name)
print(father_name)
print(dob)
print(education)
print(skills)
print(experience)
print(goal)

print("------------------------------------------------")

# 3. Write a program in which use all the operators we can use in Python
# Write your code here
# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)        
print("Subtraction:", a - b)      
print("Multiplication:", a * b)  
print("Division:", a / b)        

# Comparison Operators
print("Equal:", a == b)          
print("Not Equal:", a != b)      
print("Greater Than:", a > b)    
print("Less Than:", a < b)       

# Logical Operators
x = True
y = False

print("AND:", x and y)           
print("OR:", x or y)             
print("NOT:", not x)   

print("------------------------------------------------")

# 4. Completes the following steps of small task:
#     - Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
#     - Mention Variable of Total Marks and assign 300 to it
#     - Calculate Percentage
# Write your code here
english = 85
islamiat = 90
maths = 95
total_marks = 300
obtained_marks = english + islamiat + maths
percentage = (obtained_marks / total_marks) * 100
print("Percentage:", percentage, "%")

print("------------------------------------------------")

