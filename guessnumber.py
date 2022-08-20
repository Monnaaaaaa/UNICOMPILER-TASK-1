import os
import random
import math
os.system('cls')
player_name = input("Hello, what is your name? ")
print('I\'m glad to meet you {}!\nWelcome to number guessing game.A random number will be generated depending upon the input range and you will have to guess it.\n'.format(player_name))

def game():
        print('Now enter the range')
        first = int(input())
        last= int(input())
        x = random.randint(first,last)
        y=round(math.log(last - first + 1, 2))
        print("\nYou've only ",y," chances to guess the number!\n")

        c=0
        while c < y:
            c+= 1


            guess = int(input("Guess a number:- "))

            if guess == x:
                print("Congratulations,You Won! You did it in ",c, " try")
                play= input('Do you want to play again? "y" or "n": ')
                if play == 'y':
                    game()
                elif play == 'n':
                    print('Have a good day')
                    exit()
                else:
                    print('Invalid Input!')
                    break

            elif c < y and guess != x:

                if x > guess:
                    print("You guessed too small!")
                if x < guess:
                    print("You guessed too high!")
                if (x%2 == 0):
                    print('It is an even number')
                if(x%2!=0):
                    print('It is an odd number')
                 

            else:
                 print("You are out of guesses. You loose!")
                 print("\nThe number is %d" % x)
                 play= input('Do you want to play again? "y" or "n": ')
                 if play == 'y':
                    game()
                 elif play == 'n':
                    print('Have a good day')
                    exit()
                 else:
                    print('Invalid Input!')
                    exit()

            
game()




           
    
