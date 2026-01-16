# 1. Print Hello Python
print("Hello Python")


# 2. Print your name
name = "Sanket"
print("My name is", name)


# 3. Add two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The sum is:", num1 + num2)


# 4. Subtract two numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Difference:", x - y)


# 5. Multiply two numbers
m = float(input("Enter first number: "))
n = float(input("Enter second number: "))
print("Product:", m * n)


# 6. Divide two numbers
p = float(input("Enter first number: "))
q = float(input("Enter second number: "))
print("Division:", p / q)


# 7. Find remainder
p = float(input("Enter first number: "))
q = float(input("Enter second number: "))
print("Remainder:", 17 % 3)


# 8. Check even or odd
num = 8
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 9. Check number is greater than 10
num = 12
if num > 10:
    print("Greater than 10")
else:
    print("10 or less")


# 10. Area of a Circle
import math
radius = float(input("Enter radius: "))
area = math.pi * (radius ** 2)
print(f"The area is: {area:.2f}")


# 11. Sum of numbers from 1 to 5
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)


# 12. Print first 5 even numbers
for i in range(2, 11, 2):
    print(i)


# 13. Count characters in a string
text = "Python"
print("Length:", len(text))


# 14. Reverse a string
text = "Hello"
print("Reversed:", text[::-1])


# 15. Check string is empty or not
text = ""
if text == "":
    print("String is empty")
else:
    print("String is not empty")


# 16. Find maximum of two numbers
a = 25
b = 40
print("Maximum:", max(a, b))


# 17. Convert minutes to seconds
minutes = 5
seconds = minutes * 60
print("Seconds:", seconds)


# 18. Check if number is positive
num = 7
if num > 0:
    print("Positive number")
else:
    print("Not positive")


# 19. Print square of numbers from 1 to 5
for i in range(1, 6):
    print(i, "square is", i * i)


# 20. Simple function to greet user
def greet(name):
    print("Hello", name)

greet("User")
