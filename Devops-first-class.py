
'''
A.
1. Create a variable name first with value 7.
2. Create a variable name second with value 44.3.
3. Print result of adding first to second.
4. Print result of multiplying first by second
5. Print result of dividing second by first
'''

first = 7
second = 44.3
print (f"result = {first + second}")
print (f"result = {first * second}")
print (f"result = {second / first}")


#B results:
a= 9
c= 15
b= 8


# C results:
# No difference , "" or '' both got input of the same string.
# A string is a sequence of characters, which is marked in a single/ double quotes:


# can only concatenate str (not "int") to str
# edit suggestions:
print("result is:" + str(my_number))
print(f"result is: {my_number}")


#E
x = 1
y = 2
if x > y:
    print("BIG")
else:
    print("small")


#F
import random
num = random.randint(1, 4)
if num == 1:
    print("summer")
elif num == 2:
    print ("winter")
elif num == 3:
    print("fall")
else:
    print("spring")


# Challenge
a = 8
b = "123"
print(a+int(b))







