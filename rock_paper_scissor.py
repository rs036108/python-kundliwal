import random
l=["rock, ","scissor","paper"]
while True:
    ui=int(input('''
    ************
    Game Start
    ************
    1.Yes
    2.No|exit
     '''))
    if ui==1:
        for a in range(1,6):
            UI=int(input('''
            1. Rock
            2.Scissor
            3.Paper
            '''))
            if UI==1:
                choise="rock"
            elif UI==2:
                choise=="scissor"
            elif UI==3:
                choise=="paper"
            computer=random.choice(l)
            print(choise)
            print(computer)