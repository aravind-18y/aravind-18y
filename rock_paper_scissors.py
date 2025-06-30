import random

print("WELCOME TO ROCK.PAPER.SCISSORS")
print("\n\nenter your options by following rules")
print("\n\n>r=ROCK")
print("\n>p=PAPER")
print("\n>s=SCISSORS\n\n")
computer = random.choice([-1,0,1])
youstr = input("enter your choice:")
youDict = { "r":-1,"p":0,"s":1}
computerDict = { -1:"rock",0:"paper",1:"scissors"}

you = youDict[youstr]

print(f"your choice is {computerDict[you]}\ncomputer choice is {computerDict[computer]}")

if(computer == you):
    print("DRAW, try again")

else:
    if(computer == -1 and you == 0):
        print("YOU WINS")
    elif(computer == -1 and you == 1):
        print("COMPUTER WINS")
    elif(computer == 0 and you == -1):
        print("COMPUTER WINS")
    elif(computer == 0 and you == 1):
        print("YOU WINS")
    elif(computer == 1 and you == -1):
        print("COMPUTER WINS")
    elif(computer == 1 and you == 0):
        print("YOU WINS")

    else:
        print("somthing went wrong :(  ,try again.")