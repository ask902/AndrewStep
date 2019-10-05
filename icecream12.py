import random

'''
Practice exercises for lesson 4 of beginner Python.
'''

# Level 1
# Ask the user if they want ice cream.
# If the user says no, keep asking!
# If the user says yes, print "yay!"


# Level 2
# Goal: determine which numbers are even.
# Ask the user how many numbers we should check
# Use a loop to iterate through the numbers between 0 and the number of the user input
# Hint: use the modulus operator -> # % 2 == 1 means that the number is odd and # % 2 == 0 means the number is even

#num = int(input("Input a positive number greater than 0. "))



# Level 3
# Print out all the prime numbers between 0 and a value that the user inputs.
# Use the % operator again to determine if a number evenly divides into another number.
# Use a nested loop to check each number.

#num = int(input("Input a positive number greater than 0. "))
x = int(input("type in a positve number"))
i = 2 
is_prime = True
while i < x:
    if x % i = 0:
        is_prime = False
    i +=1

print('x is prime ==",is_prime')
