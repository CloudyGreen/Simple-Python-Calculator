#Import NumPy package
import numpy as np

#Defining four basic operations: add,subtract,multiply and divide
def add (A,B):
  return (A+B)

def subtract (A,B):
  return (A-B)

def multiply (A,B):
  return (A*B)

def divide (A,B):
  return (A/B)


#Print the instruction and operation menu for user to choose from
print ("Welcome to use this boring calculator created by Yanjun :)")
print ("Please choose which operation you will use: ")
print ("1:Add")
print ("2:Subtract")
print ("3:Multiply")
print ("4:Divide")

#User's choice should be 1/2/3/4
choice = input("Enter Choice (1/2/3/4)")

#Let user to input 2 numbers into the calculator
A = int(input("Enter Number 1 Here: "))
B = int(input("Enter Number 2 Here: "))

#Based on different choice, the calcultor will do different calculate
if choice == "1":
  print (A, "+", B ,"=", add(A,B))
  print ("Thanks for using this super duper boring calculator")

elif choice == "2":
  print (A,"-",B,"=",subtract(A,B))
  print("Thanks for using this super duper boring calculator")


elif choice == "3":
  print (A,"*",B,"=",multiply(A,B))
  print("Thanks for using this super duper boring calculator")
    
elif choice == "4":
  print (A,"/",B,"=",divide(A,B))
  print("Thanks for using this super duper boring calculator")

else:
  print ("There is an error with your import, please try another number")
  print("Thanks for using this super duper boring calculator")
