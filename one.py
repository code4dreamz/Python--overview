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




