import random

randomNumber = random.randint(1, 100)

userGuess = None
guesses = 0
while (userGuess != randomNumber):

    userGuess = int(input("Enter Your number to guess:--->>>>>  "))

    if userGuess > randomNumber:
        print("Lower Number plese")

    elif userGuess < randomNumber:
        print("Higher Number plese")

    elif userGuess == randomNumber:
        print("You have gussed the correct number")

    guesses += 1

print(f"You gussed the number in {guesses} gusses")

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())
    
if (guesses<hiscore):
    print("you have just broken high score!!!! Hip Hip Hurrey")
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses))

