import random
n=random.randint(1,100)
print("The number of guessesis total 8.\n")
i=0
while i<=8:
    x=int(input("\nEnter an number :"))
    if n>x:
        print("Your number is less.")
    elif n<x:
        print("Your number is greater.")
    else:
        print("You find your number.")
        print("You will win in ",i," steps")
        break
    i=i+1
    print("The guesses Left are ",8-i)

else:
    print("You Lose...Game Over.")
    print("The guess number is ",n)


