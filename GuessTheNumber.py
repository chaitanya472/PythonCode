import random

number = random.randint(1, 10)
print ("Guess a number between 1 and 10 you have 3 guesses")
guess1 = int(input('What is your first guess: '))
if (guess1 > number):
    print('Your guess was too high guess again')
elif (guess1 < number):
    print ('You guess was too low guess again')
else:
    print ('Congrats you got it correct')
    guess2 = number
    guess3 = number
if (guess1 != number):
    guess2 = int(input('What is your second guess: '))
    if (guess2 > number):
        print('Your guess was too high guess again')
    elif (guess2 < number):
        print ('You guess was too low guess again')
    else:
        print ('Congrats you got it correct')
        guess3 = number
if(guess2 != number):
    guess3 = int(input('What is your third guess: '))
    if (guess3 > number):
        print('Your guess was too high guess again')
    elif (guess3 < number):
        print ('You guess was too low guess again')
    else:
        print ('Congrats you got it correct')
if(guess3 != number):
        print("Sorry you're out of guesses")

