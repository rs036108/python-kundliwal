import random
while True :
    cnumber=random.randrange(1,11)
    unumber=int(input("Enter your number:--------"))
    if unumber>cnumber :
        print("Your number is high ")
        print("Compuert number",cnumber)
    elif cnumber>unumber :
        print("You number is low")
        print("Compuert number", cnumber)
    elif cnumber==unumber :
        print("You win, You gass  the number")
        print("Compuert number", cnumber)
