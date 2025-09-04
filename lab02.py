#create variables
name = "Luke"
age = 70
height = 5.5
favorite_color = "Red"

#Print one at a time
print(name)
print(age)
print(height)
print(favorite_color)

#Print with one print statement and commas
print(name,age,height,favorite_color)

#Print with Python formats or format specifiers
print(f"Hello, my name is {name} and my favorite color is {favorite_color}.")
print(f"I am {age} years old and {height}.")

#Print with format specifiers within a multi-line string
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}""")

#Create new variable
radius = 5
circle_area = 3.14 * radius **2
print(f"Circle area: {circle_area:.1f}")

#Part 2: Statements and modules

import math

 #square root of age
print (f"Square root of age: {math.sqrt(age):.2f}")

#Sine cosine of height
print (f"Sine of height: {math.sin(height):.3f}")
print (f"cosine of height: {math.cos(height):.3f}")

#part 3 Expressions and Operators
#Arithmetic operations
print(f"Age + 5 = {age + 5}")
print(f"Height - 4 = {height - 4}")
print(f"Age * Height = {age * height}")
print(f"Height / 2= = {height / 2}")
print(f"Age % 3 = {age % 3}")
print(f"Age **2 = {age ** 2}")

#part 4 Temperature Conversion
fahrenheit = float(input("Enter temperature in fahrenheit: "))
Celsius = (fahrenheit - 32) * 5/9
print(f"fahrenheit = {Celsius:.2f}")