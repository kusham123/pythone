import random
randNumber =random.randint(1,5)
print(randNumber)
userGuess =None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("enter your guess:"))
    if(userGuess == randNumber):
        print("You guesses it right !")
    else:
        if(userGuess>randNumber):
            print("You guesses it worng! Enter a smaller numbeer")
        else:
            print("You guesses it worng! Enter a larger numbeer")

        # guesses += 1
print(f"you gussess the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("you have just broken the high score")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))