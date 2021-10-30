
import math
import decimal
import os
import sys

print(

    """\nWelcome to a free and simplecalculator."""

"""\n----------------------------"""


"""\nThis calculator lets you do Addition, Subtraction, Multiplication, and Division """

"""\n----------------------------"""

)


firstnumber = int(input("The first number: "))

print("----------------------------")

secondnumber = int(input("The second number: "))




print("----------------------------")
operation = input("""Please Select the operation you want too do.
A = Addition
B = Subtraction
C = Multiplication
D = Division
----------------------------
""").lower()

print("----------------------------")
if operation == ("A").lower():
    print(firstnumber , "+" , secondnumber , "=" , firstnumber + secondnumber)

print("----------------------------")
if operation == ("B").lower():
    print(firstnumber , "-" , secondnumber , "=" , firstnumber - secondnumber)

print("----------------------------")
if operation == ("C").lower():
    print(firstnumber , "*" , secondnumber , "=" , firstnumber * secondnumber)
print("----------------------------")
if operation == ("D".lower()):
    print(firstnumber , "/" , secondnumber , "=" , firstnumber / secondnumber)