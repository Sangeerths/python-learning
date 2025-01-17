import random
secret_number=random.randint(1,20)
print("Guess a number")
for secret in range (1,7):
    
    guess=int(input())
    if(guess<secret_number):
        print("THe number you guessed is low")
        print("Guess again")
    elif(guess>secret_number):
        print("THe number guesssed is too high")
        print("Guess again")
    else:
        break
if(guess==secret_number):
    print("The number you have guessed is correct. It is "+(str(secret_number)))
