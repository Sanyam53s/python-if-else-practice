"""1. n = int(input("enter a number:"))
if n>=0:
    print("positive")
"""
"""2. n= int(input())
if n>=18:
    print("eligible for vote")"""
"""3. n=int(input("enter a number:"))
if n%7==0:
     print("Divisible by 7")"""

"""4. n =int(input("enter a number:"))
if n>=40:
     print("pass")"""


"""5. n = int(input("Enter a number: "))
if n > 100:
    print("Greater than 100")"""

""" 6. text = input("enter a string:")
if len(text)>8:
    print("Length is more than 8")"""

""" 7. temp = int(input("Enter temperature: "))
if temp > 45:
    print("Temperature is too high") """

""" 8. password = input("Enter password: ")
if password == "admin123":
    print("Logged In")"""

""" 9. n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Multiple of 10") """

""" 10. balance = int(input("Enter balance: "))
minimum = 1000
if balance < minimum:
    print("Warning: Balance below minimum limit")"""

""" 11.  n=int(input("enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")
14. Print Pass or Fail based on marks
python
Copy code
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
15. Check whether a number is positive or negative
python
Copy code
n = int(input("Enter a number: "))

if n >= 0:
    print("Positive")
else:
    print("Negative")
16. Check whether a character is vowel or consonant
python
Copy code
ch = input("Enter a character: ").lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")
17. Check if a year is leap or not
python
Copy code
year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
18. Print Valid or Invalid Password
python
Copy code
password = input("Enter password: ")

if password == "admin123":
    print("Valid Password")
else:
    print("Invalid Password")
19.  Determine whether salary is taxable or not
python
Copy code
salary = int(input("Enter salary: "))

if salary > 250000:
    print("Salary is taxable")
else:
    print("Salary is not taxable")
20.  Check whether a number is greater than 50 or not
python
Copy code
n = int(input("Enter a number: "))

if n > 50:
    print("Number is greater than 50")
else:
    print("Number is 50 or less")

21. Find the largest of three numbers
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

22. Check whether a number is positive, negative, or zero
n = int(input())

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

23. Assign grades
marks = int(input())

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

24. Check triangle type
a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

25. Check character type
ch = input()

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

26. Electricity bill (slab-wise example)

Units:

≤100 → ₹5/unit

101–200 → ₹7/unit

200 → ₹10/unit

units = int(input())

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity Bill:", bill)

27. Validate login using username and password
username = input()
password = input()

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

28. Check student result (3 subjects)
m1 = int(input())
m2 = int(input())
m3 = int(input())

if m1 >= 40:
    if m2 >= 40:
        if m3 >= 40:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")

29. Find the second largest number among three
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a < c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
else:
    if b < c:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)

30. Check loan eligibility

Conditions:

age ≥ 21

salary ≥ 25,000

credit score ≥ 700

age = int(input())
salary = int(input())
credit = int(input())

if age >= 21:
    if salary >= 25000:
        if credit >= 700:
            print("Eligible for Loan")
        else:
            print("Low Credit Score")
    else:
        print("Low Salary")
else:
    print("Age Not Eligible")"""












