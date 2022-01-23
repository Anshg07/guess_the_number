import numpy as np
from numpy import random as r

key="y"
print("-------GUESS THE NUMBER BY ~ANSH--------")
print("HEY USER WELCOME TO NUMBER GUESSING GAME!!!\n PLEASE ENTER YOUR NAME BELOW:\n")
name=input()
a=name.upper()
print("WELCOME ",a,"!!!\n LET\'S START THE GAME:\n PLEASE SELECT THE MODE OF PLAY.\nAUTO:NUMBER WILL BE GUESSED RANDOMLY\nMANUAL:NUMBER WILL BE GUESSED FROM GIVEN NUMBERS.\n 1.AUTO(COMPUTER)\n 2.MANUAL\n(auto/manual)")
m=input("ENTER YOUR MODE : ")
def auto(key):
    while(key=="y" or key=="Y"):
        x=r.randint(10)
        print("OKAY!! ",a," HERE WE GO/----\nI HAVE CHOOSE A NUMBER \'BETWEEN 1-10\' \n NOW YOU HAVE 5 CHANCES TO GUESS THE NUMBER!!!\n ALL THE BEST BUDDY!!!")
        for i in range(5):
            g=int(input("PLEASE GUESS THE NUMBER BELOW.....\n"))
            if x==g:
                print("WOAH!!! YOU WIN THE GAME !\nYES I AM THINKING ABOUT THE NUMBER ",x,"\n YOU ARE GENUIS",a,"!!!")
                break
            else:
                print(" NAHH!!TRY AGIAN...")
        if x!=g:
            print("WELL...I WAS THINKING ABOUT THE NUMBER",x,"\n I WISH YOU A BETTER LUCK NEXT TIME!!")
        key=input("WANT TO PLAY AGAIN?(y/n)\n")
    print("Thank You To Play My Game")

def manual(key):
    while(key=="y" or key=="Y"):
        print("GIVEN NUMBERS SHOULD BE MORE THEN 5 NUMBERS !")
        print("Please input below the manual set of numbers to choose from ...")
        x=list(map(int,input().split()))
        if len(x)>5:
            y=r.choice(x)
            print(y)
            print("OKAY!! ",a," HERE WE GO/----\nI HAVE CHOOSE A NUMBER FROM YOUR PROVIDED LIST! \n NOW YOU HAVE 5 CHANCES TO GUESS THE NUMBER!!!\n ALL THE BEST BUDDY!!!")
            for i in range(5):
                g=int(input("PLEASE GUESS THE NUMBER BELOW.....\n"))
                if y==g:
                    print("WOAH!!! YOU WIN THE GAME !\nYES I AM THINKING ABOUT THE NUMBER ",y,"\n YOU ARE GENUIS",a,"!!!")
                    break
                else:
                    print(" NAHH!!TRY AGIAN...")
            if y!=g:
                print("WELL...I WAS THINKING ABOUT THE NUMBER",y,"\n I WISH YOU A BETTER LUCK NEXT TIME!!")
        else:
            print("NUMBERS ARE NOT ENOUGH TO PLAY! PLAESE ENTER MORE THAN 5 NUMBERS NEXT TIME!!")
        key=input("Want to continue?(y/n)\n")
    print("Thank You To Play My Game")

if m in ["auto","AUTO"]:
    print(auto(key))
elif m in["manual","MANUAL"]:
    print(manual(key))
else:
    print("RUN THE GAME AGAIN AND CHOOSE THE CORRECT OPTION!!")
