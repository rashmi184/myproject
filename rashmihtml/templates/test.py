from turtle import *
Total_numbers=int(input("Enter the number of natural numbers to be printed:"))
start_value=1
print("The number of natural numbers are:")
while start_value<=Total_numbers:
    print(start_value)
    start_value+=1

print("Program to calculate the sum of n natural numbers")
n=int(input("Enter the value of n:"))
k=1
sum1=0
while k<=n:
    sum1=sum1+k
    k=k+1
print("Sum of series:",sum1)