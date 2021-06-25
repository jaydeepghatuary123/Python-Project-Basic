l=['s','w','g']

print("Welcome to the Snake Water Gun Game \n")
import random
n=int(input("Number of times you play with computer is "))

com=0
use=0
while n>=1:
    x=random.randint(0,2)

    print("Enter Snake for s, Water for w, and Gun for g :")
    c=input()
    if c!='s' and c!='w' and c!='g':
        print("Invalid enter  by the user...")
        break   
    if l[x]=='s' and c=='w':
        print("Computer won")
        com+=1
    elif l[x] == 's' and c == 'g':
        print("you won")
        use+=1
    elif l[x] == 'w' and c =='g':
        print("Computer won")
        com+=1
    elif l[x] == 'w' and c == 's':
        print("you won")
        use+=1
    elif l[x] == 'g' and c == 's':
        print("Computer won")
        com+=1
    elif l[x] == 'g' and c == 'w':
        print("You won")
        use+=1
    else:
        print("Match Draw")
    n-=1

print("The Result is between Computer and user is :")

if com>use:
    print("\nComputer winner at last.")

elif com<use:
    print("\nUser winner at last.")

else:
    print("\nMatch Draw No one can won.")


























