'''
Ques 1: Write a program to input 2 numbers & print their sum ?
'''

first = int(input("enter first:"))
second = int(input("enter second:"))
print("sum=",first+second)

'''
 result :enter first:5
         enter second:4
         sum= 9
'''
'''
Ques 2 :Write a program to input side of a square & print its area ?
'''

side = float(input("enter square side:"))
print("area = ",side*side)

'''
result :enter square side:5
area =  25.0
'''
'''
Ques3: Write a program to input 2 floating point numbers & print their average?
'''
a = float(input("enter first :"))
b = float(input("enter second :"))
print("avg =",(a+b)/2)

'''
result :enter first :16.5
enter second :3.5
avg = 10.0
'''

# Conditonal Expression

mark = int(input("enter student mark :"))

if(mark >= 90):
    grade = "A"
elif(mark >= 80 and mark < 90):
    grade = "B"
elif(mark >= 70 and mark < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student ->",grade)

'''
Result :enter student mark :98
grade of the student -> A
enter student mark :85
grade of the student -> B
enter student mark :55
grade of the student -> D
'''



# length of string and concatenation
str1 = "apna"
len1 = len(str1)
print  (len1)

str2 = "college"
len2 = len(str2)
print (len2)

final_str = str1 + " " + str2
print(final_str)

'''
result : 4
        7
        apna college
        '''

# Ques : write a program to input user's first name & print its length ?


name = input("entr your name :")
print("length of your name is ",len(name))

'''
result : entr your name :subeer
         length of your name is  6
         
# Ques : write a program to check if a number entered by the user is odd or even ?


num  = int(input("enter number:"))

if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")
'''
result: enter number:4
        EVEN
        enter number:5
        ODD
'''

# Ques : WAP to find the greatest of 3 numbers entered by the user ?

a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number"))

if(a >= b and a >= c):
    print("first number is largest",a)
elif(b >= c):
    print("second number is largest",b)
else:
    print("third is largest",c)

'''  
result :
enter first number :5
enter second number :12
enter third number2
second number is largest 12
'''














