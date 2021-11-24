"""
Write a program that takes from the user a number A and B (B ≤ A). Print all numbers from A to B inclusively horizontally in descending order
"""
numA = int(input("Give me a number to range from? "))
numB = int(input("Give me a number to range to? "))
for i in range(numA,numB - 1,-1):
  print(i, end = " ")