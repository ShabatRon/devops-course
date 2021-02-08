'''A.
1. Create two variables name X and Y.
2. Print “BIG” if X is bigger than Y .
3. Print “small” if X is smaller than Y.
'''

x = 1
y = 2
if x > y:
    print("BIG")
else:
    print("Small")

'''B.
1. Run a “for” loop 5 times.
2. Print iteration number every time. 
'''

for i in range(5):
    print(f"Iteration num:{i}")

'''
C.
1. Create a variable and initialize it with a number 1-4.
2. Create 4 conditions (if-elif) which will check the variable.
3. print the season name accordingly: 
- 1 = summer
- 2 = winter
- 3 = fall
- 4 = spring 
'''
import random

num = random.randint(1, 4)
print(f"num:{num}")
if num == 1:
    print("summer")
elif num == 2:
    print("winter")
elif num == 3:
    print("fall")
else:
    print("spring")

'''
D.
1. how many times will the following loop run?  {10}
2. what will be printed last? {10}


'''

count = 1
while count < 11:
    print(count)
    count += 1

'''
Write a program with variables holding the following:
1. Your age.
2. First letter of your last name.
3. Current shekels-dollar currency.
4. Did you flew abroad (true/false)
5. Your apartment number.
● Print all variables.
● Add the currency to your age, and check the result. 
'''

age = input("1. write your age")
letter = input("2. First letter of your last name")
currency = input("3. Current shekels-dollar currency.")
abroad = input("4. Did you flew abroad (true/false)")
apartment_num = input("5. Your apartment number.")
print(f"age:{age}, letter:{letter} , currency:{currency}, abroad:{abroad}, apartment number:{apartment_num}")
print(int(age) + float(currency))

'''
F.
Create a program which uses input with the following:
1. Ask user for his phone number
2. Print the words “phone number” and the phone number the
user entered. 
'''

phone_num = input("enter you phone number", end=" ")
print(f"phone number: {phone_num}")

'''
G.
 Write a program with the following:
1. Method named printHello() that prints the word “hello”.
2. Method named calculate() which adds 5+3.2 and prints the
result. 
'''


def print_hello():
    print("hello")


def calculate():
    print(5 + 3.2)


print_hello()
calculate()

'''
H.
Write a program with the following:
1. Method that receive your name and prints it.
2. Method that receive a number, divide it by 2, and prints the
result.
'''


def print_name(your_name="Ron"):
    print(f"your name is: {your_name}")


def dev_by_two(num):
    print(num / 2)


'''
I.
Write a program with the following:
1. Method that receive two numbers, add them, and return the
sum.
2. Method that receive two Strings, add space between them,
and return one spaced string.
'''


def sum_of_num(num1, num2):
    return num1 + num2


def cat_strings(str1="str1", str2="str2"):
    return str(str1) + " " + str(str2)


'''
K.
Create a nested for loop (loop inside another loop) to create
a pyramid shape: 
'''

for i in range(10):
    for j in range(i):
        print("#", end=" ")
    print()

'''
Create a nested for loop to create X shape (width is 7,
length is 7):
'''

for i in range(1, 7):
    print("#")
    for j in range(1, i):
        print("$")

'''
Write a program with the following:
1. Method that gets a number from the user (using input).
2. Method that receive the number from the first method, and
computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7) 
'''


def get_num():
    num = input("please enter a number")
    return int(num)


def sum_of_digits(get_num):
    num = get_num()
    sum_of_digits = 0
    while (num / 10 > 0):
        print(f"{sum_of_digits} + {num % 10}")
        sum_of_digits = sum_of_digits + (num % 10)
        num = (num // 10)
    return sum_of_digits


r = sum_of_digits(get_num)
