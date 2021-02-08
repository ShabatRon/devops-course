
'''
1. Write the following code: a = 1/0;

2. Build a corresponding try-except block to
avoid exception.
'''

try:
    a = 1/0
except ZeroDivisionError:
    print('Exception: division by zero')
    a = input("please set another input to a")




#3. Is the following code legal?
try :
 x = 1
finally :
 print("finally") 
'''
## Is the following code legal? Yes

#4
. What exception types can be caught by the
following handler?
Except:
'''
# Answer: all types of exceptions


#5
'''What is wrong with using the above type of
exception handler?'''
# Using global exception can caught too many exception-scenarios. sometime you want the code to failed with exception a cpecialy when you did not expect to get it.


#6
'''What exceptions can be caught by the
following handlers?'''
try:
    write_to_file = open("C:\\sdfusdhfo\\")
except IOError as e:
    print(e)

try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(e)


#7-10 work with files

file_path = "C:\\ron\\Python-learning\\words.txt"
content = "my name is Ron Shabat"

write_to_file = open(file_path, 'w', encoding='utf-8')
write_to_file.writelines(F"{content} \n")
write_to_file.close()

write_to_file = open(file_path, 'a', encoding='utf-8')
write_to_file.writelines("שם בעברית: רון שבת")
write_to_file.close()

read_from_file = open(file_path, encoding='utf-8')
for line in read_from_file.readlines():
    print(line)
read_from_file.close()








