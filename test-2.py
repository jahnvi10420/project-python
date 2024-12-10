"""
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
"""


"""
marks = float(input("Enter your marks: "))

if marks >= 33:
    print("pass")
else:
    print("fail")
"""


myNum = 5

def logic():

    guessNum = int(input("Guess the number between 0 to 10: "))

    if guessNum > myNum:
        print("go lower")
        logic()
    elif guessNum < myNum:
        print("go higher")
        logic()
    elif guessNum == myNum:
        print("You are right, thnku for playing!")

logic()