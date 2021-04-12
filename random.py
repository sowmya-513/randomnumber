import random
import math
 # Taking Inputs
l= int(input("Emter a number:- ")) 
 
# Taking Inputs
u = int(input("Enter a number:- "))  
 
# generating random number between
# the lower and upper
x = random.randint(l, u)
print("\n\tYou have only ", round(math.log(u-l+ 1, 2))," chances to guess the number\n")
 
 # Initializing the number of guesses.
count= 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(u-l+1, 2):
    count += 1
     
     # taking guessing number as input
    guess = int(input("Guess a number: ")) 
     
    # Condition testing
    if x == guess:  
       print("Congrats you did it in ", count, " try")
       # Once guessed, loop will break 
       break
    elif x > guess:
       print("You guessed too small!")
    elif x < guess:
       print("You Guessed too high!")
 
# If Guessing is more than required guesses, 
# shows this output.
if count >= math.log(u-l+ 1, 2):
   print("\nThe number is %d"%x)
   print("\tBetter Luck Next time!")
