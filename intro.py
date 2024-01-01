#-------------------------------------Intro to Python (reference APNA COLLEGE YOUTUBE VIDEO)---------------------------

# -------------------strings
# print('hello world')

# -------------------variables

# x=123  #integer

# y="heyy navv"

# z=34.0 #float

# d= x>z #boolean

# print(x , y , z ,d)

#---------------taking user inputs

# name=input("Enter your name :")

#concatenation

# print("Heyy " + "" + name)

#----------------type conversions

# str()
# bool()
# float()


# old_age =input("Enter your old age : ")
# new_age = int(old_age) + 4
# new_age = old_age + str(4)
# print(new_age)

#adding numbers

# first_num=input("Enter first number : ")
# second_num=input("Enter second number : ")
# result=int(first_num) + int(second_num)
# print( "The sum is "+  str(result))


#------------methods in stings--------------------

# name = "Noor Kaur"
# print(name.find("s"))
# print(name.replace("Noor Kaur", "kutti"))

#-------------keywords--------------------------------

# print("N" in name)

#--------------------Arithmetic operators-------------
#  + , - , * , / , //(removes decimal value) , % (remainder opt) , **(power opt)

#---------------------------shortcuts
# i = 5
# i += 5 ; i *= 2
# print(i)

#----------------------operator precedence-------------------
 
# result= 2+4 * 10
# * > + , / > + , () > * / 
# print(result)

#-----------------------comparison operators-------------------
# > , < , >= , <= , == (compare values) , !+
# print ( 3==2)

#---------------------logical operators---------------------
#  or , and , not 


#----------------------------conditional statments--------------

#if else statements
# age =int(input("Enter any age : "))
# if(age>=18):
#     print(" Wohhooooo You can drink alcohol & drive.....")
# elif(age<18 and age >10):
#     print (" Sryyyyy You can't even drink alcohol right now... ")
# else :
#     print("You are kid ")

#----------------------------mini project ( calculator)----------------------------------

# num1 = int(input("Enter 1st num : "))
# opt = input("Enter operator (+ , - , * , / ,%)' : " )
# num2 = int(input("Enter 2nd num : "))
# if opt == "+" :
#     print(num1 + num2)
# elif opt == "-" :
#     print(num1 - num2)
# elif opt == "*" :
#     print(num1 * num2)
# elif opt == "/" :
#     print(num1 / num2)
# elif opt == "%" :
#     print( num1 % num2)
# else:
#     print("Invalid operation")


# ---------------------range --------------------------

# range(5) #0 , 1 ,2 ,3 , 4,
# r= range(6) #kindof sequence of numbers
# print(r)

#------------------------loops---------------------

#while loop ~~~~~~ whenever the condition is true it will execute

# i=1
# while i<=5:
#     print(i* "*")
#     i=i+1

# i=5
# while i>=0:
#     print(i* "*")
#     i=i-1

#forloops ~ to iterate over a list

# for i in range(1,20,2):
#     print(i)
# for i in range(20,1,-2):
#     print(i)

#------------------------lists--------------------
#collection of items

# marks = [96 , 76 , 89 , 90 , "maths"]
# print(marks)
# print(marks[2])
# print(marks[-1]) # denotes last item or counting in  reverse order
# print(marks[0:2])

#iterate using for loop
# for score in marks:
#     print(score)

#operations on list
# marks.append(100)
# marks.insert(0,"nav")  #add item at end
# print(marks)
# print(len(marks))  #prints length of list

#using while loop in list
# i = 0
# while i < len(marks):
#     print(marks[i])
#     i=i+1

# marks.clear()
# print(marks)

#------------------break and continue ------------------------

# students = ["Nav" , "Noor" , "Haruuu" , "Shalzziee"]
# for stu in students:
#     # if stu =="Haruuu":
#     #     break;
#     # print(stu)

#     if stu =="Shalzziee":
#         continue;
#     print(stu)


#-------------------tuple-----------------
#similar to list but its immutable (can't change the values)

# marks =(12, 34, 56, 77, 12 , 12)
# #operations
# print(marks.count(12))
# print(marks.index(12))

# person = 'nav' ,'harleen' , 'gurleen'
# print(person)  #by default acts as tuple no need to use round brackets

#-----------------------sets--------------------
# collection of unique elements
#un-ordered
#indexing dosen't exist in sets

# marks={ 67, 78 ,89, 90 , 90}
# print(marks)
# for score in marks:
#     print(score)

#-----------------------dictionary-------------------
#similar to sets , store key values as key-value pair

# marks={"English":98, "chemisrty":89}
# print(marks["chemisrty"])
# marks["physics"]=87;
# print(marks)

# marks["physics"]=99;
# print(marks)

#-----------------functions------------------
# 1) In built 
    # int()
    # str()
    # bool()

# 2) Moule
    # math module 
# import math as m

# print(dir(m))

# from math import sqrt
#from math import * (for all functions)

# print(sqrt(25))


# 3) User defined
# def sum(a , b):
#     print(a + b)

# sum(45,67)


# -----------------------------------------Reference ANUJ YOUTUBE VIDEO----------------------

#reverse string~~~~~~~~~~~~ using slicing operation
# name = "Hello"
# print(name[::-1])

#------------------------creating random lists-------------------
#list comprehension
# a = [x for x in range(10)]
# a = [x for x in range(100) if x%2==0]

#--------------------modules -----------------
# file containing variable & functions
# import math
# import math as m

# from math import cos

# print(cos(3.14))

#------------------------functions---------------
# def greet(name , dish):
#      print("Gudd Mrngggg ", name)
#      print("Lets eat ", dish)
# greet("nav", "cake")

#-----------------------------File handling in python---------------------------
# file operations in folowing order ~~~~~~~~~ 1)open a file 2) read or write  3)close the file 


#open a file
# --------------------------reading a file-----------------
# f = open("data.txt" , 'r')
# print(f.read())
# f.close()

# better way to code this thing--------
# with open("data.txt") as f:
#     # for line in f:
#     #     print(line)
#     f.seek(0) #~~~~~~~~~~denotes curson
#     print(f.read())

#----------------------------------creating/writing a file using write operation-----------------------------------
# with open("write.txt" , 'w') as f:
#     f.write("Hie Navvv ~~~~~~~ we have created a file for you using write operation in python")


#append data 

# with open("write.txt" , 'a') as f:
#     f.write("Appending ")


# with open("crash.txt" , "a") as f:
#     f.write("\n Navv lets start todays session")

# with open("crash.txt" , "r") as f:
#     print(f.read())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~reference CODE WITH HARRY CRASH COURSE PYTHON (YOUTUBE VIDEO)~~~~~~~~~~~~~~~

#empty set/dict
# x = set()   #set
# y = {}      #dict
# print(type(x) , type(y))

# a = int(input("Enter a number : "))
# match a:
#     case 1:
#         print("The value is 1")
#     case 2:
#         print("The value is 2")
#     case _:
#         print('NO MATCH FOUNDD ~~~~~~~~~~~~~~~default case')

#----------------------infinite while loop

# while(True):
#     num=int(input("Enter a number : "))
#     print(num)
#     if num==0:
#         break

# print('program is finish executing')


#-----------exception handling ---------------------------

# a = int(input('Enter your number : '))

# print(a+3)

# try :
#     a = int(input('Enter your number : '))
#     print(a+3)
# except Exception as e :
#     print("Some error occcured ....," , e)


# -------------------------file handling

#writing to a file
# s = "Code with harryyyy testing---------------"
# with open("testing.txt" , "w") as f:
#     f.write(s)

#reading to a file
# with open("intro.py" , "r") as f:
#     t = f.read()
#     print(t)


#adding data to a existing file 

# d = "\n Navv are you ready to go for implementing some projects?"
# with open("testing.txt" , "a") as f:
#     f.write(d)


#-------------------------OOPS-----------------------------
# class ~ kind of a template using which we can create objects

# class Employe:
#     def __init__(self , name , salary):  #constructor function
#         self.name = name
#         self.salary = salary
#     def getSalary(self):
#         return self.salary

# x = Employe( 'harry' , 50000)
# print(x.salary)

#----------------------------------------------------Reference TELUSKO YOUTUBE CHANNEL--------------------------------------

# test = int(input('Enter a number : '))
# for i in range(2,test):
#     if test%2==0:
#         print(" Not a Prime number")
#         break
# else:
#     print("Prime number")

# import array 
# from array import*


# x = array( "i" , [])
# x = []

# n = int(input('Enter the lenth of array : '))
# for i in range(n):
#     t=int(input('Enter value : '))
#     x.append(t)
# print(x)

#------------OOPS


# ----------------------class , methods , and object ------------------
# class Computer:
#     def config(self):
#         print(" i5 , 16gb , 1tb")

# --------creating objects----------
# com1 = Computer()
# com2 = Computer()

# ---------calling an object
# Computer.config(com1)

# com1.config()  #~~~~~~ using ojbect to call a method inside a class


# ----------------- _init_ method ----------------------
# class Computer:
#     def __init__(self , cpu , ram):   # called automatically
#         self.x = cpu
#         self.y = ram

#     def config(self):
        
#         print("Config is " , self.x , self.y)

# com1 = Computer("i5" , 16)
# com2 = Computer('i10' , 30)

# com1.config()


# ------------ understanding self and constructor

# class Userdata:
#     def __init__(self):
#         self.name= "Nav"
#         self.age = 22

#         print("Get lost")

#     def update(self):
#         self.name="Noor"
    


# one = Userdata()
# two = Userdata()

# two.update()

# print(one.name)
# print(two.name)



#---------------------------------inheritance------------------------------


#----------single level inheritance
# class A :   #super class
#     def feature1(self):
#         print("Feature 1 working")

#     def feature2(self):
#         print("Feature 2 working")
# class B(A) :  #sub class  #class B is inheriting all the features of class A
#     def feature3(self):
#         print("Feature 3 working")

#     def feature4(self):
#         print("Feature 4 working")
    
# a1 = A()
# a1.feature1()
# a1.feature2()

# b1 =B()

# # b1.feature1()
# try:
#     b1.feature1()
# except Exception as e :
#     print("Please create a subclass to access the features of other class" , e)
# finally:
#     print("Program is finished")

#Types :
    
# Single level inheritance ~ superclass A > subclass B(A)

#multi-level inheritance ~ super class A > subclass B(A) > subclass C(B)
    
#Multiple inhertiance ~ super class A , subclass B , subclass C (A,B)




#-----------------------------polymorphism-------------------

# poly ~ many
# morph ism ~ forms

# objects will have multiple forms

# Ways to implement polyformism
# 1) Duck typing
# 2) Operator overloading
# 3)  Method overloading
# 4) Method Overriding














