# print("hello world")

#  varaibles
# name = "abc"
# print(name)


# _name = "abc"
# print(_name)


# nameFirst = "huma"
# print (nameFirst)

# name1st = "abc"
# print (name1st)

# name-name = "Jane"
# print (name-name)

#variables for string and number concatenation
# name = "abc"
# age = "26"
# print("hello , my name is" + " "+name+ " "+age )


# age1 = 25
# age2 = 30
# print(age1 ,age2)


# familiar and unfamiliar operator
# a = 10 
# print(a)
 
# a = 10
# a = a + 10
# print(a)

# a = 20
# a += 10
# print (a)

# math ambguity
# a = 2 + 3 * 5
# print(a)

# a = (2 + 3) * 5
# print(a)

#  if condtition
# x = 10
# if x == 10:
#     print("x is 10")
# else:
#     print("x is not 10")

# if else
# x = 60
# if x >=50:
#     print("excellent")
# elif x >=30:
#     print ("good")
# else:
#      print("fail")

# not equal operator
# hp = 10
# if(hp != 10):
#  print("healthy")
# else:
#     print("unhealthy")
# class task
# age = input ("Enter your age: ")
# age =int(age)
# print(type(age))

# Edu = input ("Enter your Education: ")
# Edu =int(Edu)
# print(type(Edu))

# height = input ("Enter your height: ")
# height =int(height)
# print(type(height))

# if(age <=18 and Edu <=14 and height <=5):
#     print("Pass")
# else:
#     print("Fail")

# input
# name = input("enter your name: ")
# print("Hello,",name)


# input if condition convert with int
# num = input("enter you num: ")
# num = int(num)
# print(type(num))
# if(num==90):
#  print("Grade A")
 

#  if test of condition using and or opeartor

# marks = input("Enter your marks: ")
# marks = int(marks)

# if(marks >= 90 and marks <= 100):
#     print("Grade A")
# elif(marks >=80 and marks <90):
#     print("Grade B")
# elif(marks>=70 and marks< 80):
#     print("Grade C")
# else:
#     print("Fail")


#  nested if condition
# num1 =10
# num2=11
# if(num1==10):
#     if(num2==11):
#         print("Both numbers are equal")
#     else:
#         print("num1 is 10")


# Lists
# name = []
# name = ["1"] + name + ["Huma"]
# name.append("shahzadi")
# name.insert(0, "humayy")
# print(type(name),name)

#Class task
# age = input ("Enter your age: ")
# age =int(age)
# print(type(age))

# Edu = input ("Enter your Education: ")
# Edu =int(Edu)
# print(type(Edu))

# height = input ("Enter your height: ")
# height =int(height)
# print(type(height))

# if((age <=18 and Edu <=14) or ( Edu <=14 and height <=5) or (height <=5 and age <= 18)) :
#     print("Pass")
# else:
#      print("Fail")

# list extends
# ls1 = [1,2,3,4,5]
# ls2 = [6,7,8,9,10]
# ls1.extend(ls2)
# print(ls1)

#Del List / index from list
# ls = [1,2,3,4,5]
# del ls[0]
# print(ls)

# Del value from list
# ls = [1,2,3,4,5]
# ls.remove(1)
# print(ls)

# slice
# ls =[1,2,3,4,5]
# ls2 = ls[2:3]
# print(ls2)

# colon 
# ls =[1,2,3,4,5]
# ls2 = ls[0:5:2]
# print(ls2)

# sorting list
# ls = [3,2,1,5,7,6]
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# pop
# ls =[1,2,3,4,5,6]
# ls.pop(2)
# print(ls)

# ls.pop(-1)
# print(ls)

# Total index
# ls =[1,2,3,,5]
# le = len(ls)-1
# print(le)

# tuple 
# tp = (1,2,3,4,5)
# print(type(tp))

# dictation
# dic ={"name":"Johan dae","age":"26"}
# print(type(dic))

# set
# st = {"johan dae",26}
# print(type(st))

# frozenset
# frst = frozenset({"hello"})
# print(type(frst))

# byte
# byt = b'hello'
# print(type(byt))

# boolen
# bln = True
# print(type(bln))

# byteArray
# bytearray = bytearray(b'hello')
# print(type(bytearray))

# none
# none = None
# print(type(none)

# Tuple
# tup = ("hello", "world")
# print(tup)

# # tuple constructor
# tup = tuple((1,2,3,4))
# print(tup)

# tuple length
# tup = (1,2,3,4)
# print(len(tup))

# tuple indexing
# tup = (1,2,3,4)
# print(tup[1])

# tuple convert into list
# tup = (1,2,3,4)
# y = list(tup)
# print(y)

# # list convert into tuple
# tup = (1,2,3,4)
# tup =tuple(y)
# print(tup)

# insertion method
# tup = (1,2,3,4)

# y =(list(tup))
# y.insert(0,"hello")
# print(y)
# tup = tuple(y)
# print(tup)

#using remove value
# tup = (1,"2",3,4)
# y =(list(tup))
# y.remove("2")
# print(y)

# Dictionaries
# thisdic = {"name": "faiza","age": 20, }
# print(thisdic["name"])
# print(thisdic)

# change in dictionary
# thisdic = {"name": "faiza","age": 20, }
# thisdic["name"] = "Dania"
# print(thisdic)

# get value from dic
# thisdic = {"name": "faiza","age": 20, }
# x = thisdic.get("name")
# print(x)
# print(thisdic)

# update 
# thisdic = {"name": "faiza","age": 20, }
# thisdic.update({"lastname":"Dania"})
# print(thisdic)

# dictionary value and key
# thisdic = {"name": "faiza","age": 20, }
# print(thisdic.values())
# print(thisdic.keys())
# print(thisdic)

# # add multiple value in same key or single key
# thisdic = {"name":"Ali", "Age": 20,"list":["A","B","C"]} 
# print(thisdic)

# Nested Dic
# parent = {
#    "Child1": {"name": "John",
#     "age": 30,},
#     "Child2" :{
#             "name": "Alice",
#             "age": 8
#               },
#     "Child3":{
#             "name": "Bob",
#             "age": 10
#         }
   
# }

# # call only  one child
# print(parent["Child1"])

# # call only  one child value
# print(parent["Child1"]["name"])

# print(parent)

# change nested value

# parent["Child1"]["name"] = "Huma"
# print(parent)

# copy same data
# parent2 = parent.copy()
# print(parent)
# print(parent2)

# Sets
# set1 = {1,2,3,4,5}
# print(set1, type(set1))

# set constructor
# set1 =set({1,2,3,4,5})
# print(set1, type(set1))

# add set but no change sequence
# set1 ={1,2,3,4,5}
# set1.add(6)
# print(set1)
# # print(len(set1))   length  
# print(len(set1)-1)   indexing
#
# update
# set1 ={1,2,3,4,5}
# set2 ={6,7,8,9,10}
# set1.update(set2)
# print(set1)

# remove element from set
# set1 ={1,2,3,4,5}
# set1.remove(2)
# print(set1)

# discard set
# set1 = {1,2,3,4,5}
# set1.discard(9)
# print(set1)

# # union of set
# set1={1,2,3,4,5}
# set2 ={5,6,7,8,9,10}
# set3 = set1|(set2)
# print(set3)

# # # intersection of set
# set1={1,2,3,4,5}
# set2 ={5,6,7,8,9,10}
# set3 = set1&(set2)
# print(set3)

# # # difference of set
# set1={1,2,3,4,5}
# set2 ={5,6,7,8,9,10}
# set3 =set1-set2
# print(set3)

# precendence
# set1={1,2,3,4,5}
# set2 ={5,6,7,8,9,10}
# set3 ={11,12,13,14,15}
# # set4 = set1& set2 |set3
# set4 = set1|set2&set3
# print(set4)

# in keyword using boolen
# set1 ={1,2,3,4,5}
# print(1 in set1)

# Ternery operator
# x = 10
# print("pass") if x ==10 else print("x is not 10")

# for loop
# for x in range(100):
#     print(x)

# add list in for loop
# li =[1,2,3,4,5]
# for x in li:
#     print(x)

# while loop
# i=0
# while i<5:
#     print(i)
#     i+=1

# break ,continue and pass statement
# for i in range(5):
#     print(i)
#     if i == 2:
#         # break
#         # continue
#         pass
    
# Nested loop
# ls1=["mango","Apple","orange","cherry"]
# ls2=["mango","Apple","orange","cherry"]
# for i in ls1:
#     for j in ls2:
#         print(i,j)

# ls1 = ["mango","Apple","orange","cherry"]
# ls2 =[]
# for i in ls1:
#     if "a" in i:
#         ls2.append(i)
#     print(ls2)

# # list comprehension
# ls1 = ["mango","Apple","orange","cherry"]
# ls2 =[]
# for i in ls1:
#     if "a" in i:
#         ls2.append(i)
#     print(ls2)
# ls3 = [i for i in ls1 if "a" in i]
# print(ls3)



# iterator and iterable
# ls = [1,2,3,4,5]
# ls2 = iter(ls)
# print(next(ls2))
# print(next(ls2))
# print(next(ls2))
# print(next(ls2))
# print(next(ls2))

# Function and varaible scope
# def s():
#      print("hello world")
# s()

#2 method
# def s():
#      return "hello"
# print(s())

# def s():
#      return "hello"
# p = s()
# print(p) 

# sum
# def sum(p):
#      print("hello world",p)
# sum(89)

# def sum(p, q):
#    print("hello world",p+q)
# sum(78,45)

# def sum(p, s):
#     print("hello world",p,s)
# sum(78,45)

# multiple value
# def sum(**q):
#      return q["name"]+" "+str(q["age"])
# print(sum(name = "john", age =25))

# variables
# s = 12
# def f():
#    p = 10
#    print(p,s)
# f()

# lambda expression
# p = lambda x : x**2
# print(p(5))

# map and filter
# def s(n):
#        if n%2 == 0:
#         return "even"
# number = [1,2,3,4,5,6,7,8,9]
# even_number = list(filter(s,number))
# print(even_number)

# Inner/nested function
# def s():
#     def t():
#         return "hello"
#     print(t())
# s()

# def s():
#     def p():
#         print("Hello world!")
#     p()
# s()

# File handling/Excaption/Error handling
# x=10
# try:
#     print(x)
# except:
#     print("An error occurred")
# else:
#     print("No error occurred")
# finally:
#     print("This is always executed")

# File handling
#write
# f = open("e.txt","w")
# f.write("this is python")

# append
# f = open("e.txt","a")
# f.write("this is python language")

# rempove
# import os
# os.remove("e.txt")

# read
# print(f:readline(5))

# close
# f.close()

# Class and Object
class Person:
       x = 10**2
p = Person()
print(p.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("John Doe", 26)
p.show()



# import numpy as np
# array1 = np.array([1,2,3,4,5])
# print(array1[1:3])




