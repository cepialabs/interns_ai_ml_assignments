#1.Add Two Numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2
print("the sum of two number is:", sum)

#2. Area_of_triangle.py
H=int(input("enter the height of the triangle:"))
B=int(input("enter the base of the triangle:"))
area = (1/2)*B*H
print("the area of triangle is:",area)

#3.check prime number
num = int(input("Enter a number: "))
if num ==1:
    print("it is not a prime number")
if num >1:
    for i in range(2, num):
        if num % i == 0:
            print (num, "is not a prime number")
            break
    else:
        print (num, "is a prime number")

#4.Celsius to fahrenheit
C = int(input("Enter temperature in Celsius: "))
F = (C * 1.8)+ 32
print("Temperature in Fahrenheit:", F)

#5.Check Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#6.Check if Positive,Negative or Zero
num =int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

#7.Check largest number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    print("The largest number is", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("The largest number is", num2)
else:
    print("The largest number is", num3)

#8.Check leap year
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#9.Factorial of a number
num = int(input("Enter a number: "))
fact = 1
if num <0:
    print("Factorial does not exist for negative numbers")
elif num ==0:
    print("The factorial of 0 is:",1)
else:
    for i in range(1,num + 1):
        fact = fact*i
    print("The factorial of num is", fact)

#10.Multiplication table
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print (num, 'x', i, '=', num*i)
    i += 1

#11.Factors of a number
num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)


#12.fibonacci sequence
a = 0 
b = 1
num = int(input("Enter number to obtain Fibonacci series up to:"))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c = a + b
        a = b
        b = c
        print(c)

#13.largest number in a list
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

#14.print all prime numbers in an interval
L = int (input("Enter lower range: "))
U = int (input("Enter upper range: "))
for num in range (L, U + 1):
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
            print (num)

#15.random number generator
import random
num = random.randint(1, 10)
print ("the random number is:",num)

#16.Square of a number
num = int(input("Enter a number: "))
sq = num*num
print(" the square of number is", sq)

#17.Square root of a number
num = int(input("Enter a number: "))
sr = num **(1/2)
print("The square root of number is", sr)

#18.Sum of elements in a list
numbers = [10, 2, 99, 40]
sum= 0

for num in numbers:
    sum += num

print("Sum of list elements:", sum)

#19.Sum of first N natural numbers
n = int(input("Enter N: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#20.Swapping two variables
num1 = int(input("Enter first variable: "))
num2 = int(input("Enter second variable: "))
temp = num1
num1 = num2
num2 = temp
print("After swapping:")
print("First variable:", num1)
print("Second variable:", num2)