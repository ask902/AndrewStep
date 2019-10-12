import random

print("Guess the number that's in my mind")
print("Hint: It's between 0 and 100")

n = random.randint(1, 100) #pick a random number from 1 through 100
tries = 0
max_tries = 10
found = 0
for i in range(1,100):
    tries += 1
    p = int(input("Enter number -> "))
    if p < n:
        print('Too low')

        
    #elif ??:

    #else:
        #print("You won in", tries, "tries!")