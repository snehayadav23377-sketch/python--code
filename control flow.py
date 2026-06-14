num = 10
if num > 0:
    print("the positive number")  
    age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    \
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
