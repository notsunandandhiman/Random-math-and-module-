

import random
playing = True
number = str(random.randint(10,20))
print("I will generate a number from 10 to 20 and you have to guess the number one digit at a time,")
print("the game ends when you get 1 hero ")


while playing:
            guess = input("Guess a digit: ")
            if number == guess:
             print("You got it right!")
             print("The number was", number)
             break
            else:
             print("Try again \n")
             