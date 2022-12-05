import random
import time

print("Human expression research #Day 01 by Sahil Thakur \n \n")

lyf = 0
lifetime=0
while True:
    head = random.randint(0,2)
    yhead = random.randint(0,2)

    tm = random.randint(3,10)
    lifetime += tm
    xmove = random.randint(0,2)
    ymove = random.randint(0,2)


############################################################################

    if head == 1:
        print("Case 1: \nCurrent Facial Expressions = ")
        print("Life Time in seconds", lifetime)
        print("Head X: ", head)
        print("Head Y ", yhead)
        print("Time : ", tm)
        print("Eye Y :",ymove)
        print("Eye X :", xmove)
        print("Head RIGHT")


        if yhead == 1:
            print("Head Postion : Y (UP)")
        elif yhead == 0:
            print("Head Postion : -Y (DOWN)")
        elif yhead == 2:
            print("Head Position : -YY Constant")
        if xmove == 1:
            print("Eye Postion : X (Right)")
        elif xmove == 0:
            print("Eye Postion : -X (Left)")
        elif xmove == 2 :
            print("Eye Postion : -XX (Constant)")
        if ymove == 1:
            print("Eye Position : Y (Up) ")
        elif ymove == 0 :
            print("Eye Postion : -Y (Down)")
        elif ymove == 2 :
            print("Eye Postion : Y-Y (Constant)")
        print("\n")
        time.sleep(tm)


###########################################################################

    elif head == 0:
        print("Case 2: \nCurrent Facial Expressions = ")
        print("Life Time in seconds", lifetime)
        print("Head X: ", head)
        print("Head Y ", yhead)
        print("Time : ", tm)
        print("Eye Y :", ymove)
        print("Eye X :", xmove)
        print("Head Constant")

        if yhead == 1:
            print("Head Postion : Y (UP)")
        elif yhead == 0:
            print("Head Postion : -Y (DOWN)")
        elif yhead == 2:
            print("Head Position : -YY Constant")
        if xmove == 1:
            print("Eye Postion : X (Right)")
        elif xmove == 0:
            print("Eye Postion : -X (Left)")
        elif xmove == 2:
            print("Eye Postion : -XX (Constant)")
        if ymove == 1:
            print("Eye Position : Y (Up) ")
        elif ymove == 0:
            print("Eye Postion : -Y (Down)")
        elif ymove == 2:
            print("Eye Postion : Y-Y (Constant)")
        print("\n")
        time.sleep(tm)

###################################################################################

    else:
        print("Case 3: \nCurrent Facial Expressions = ")
        print("Life Time in seconds", lifetime)
        print("Head X: ", head)
        print("Head Y ", yhead)
        print("Time : ", tm)
        print("Eye Y :", ymove)
        print("Eye X :", xmove)
        print("Head LEFT")

        if yhead == 1:
            print("Head Postion : Y (UP)")
        elif yhead == 0:
            print("Head Postion : -Y (DOWN)")
        elif yhead == 2:
            print("Head Position : -YY Constant")
        if xmove == 1:
            print("Eye Postion : X (Right)")
        elif xmove == 0:
            print("Eye Postion : -X (Left)")
        elif xmove == 2:
            print("Eye Postion : -XX (Constant)")
        if ymove == 1:
            print("Eye Position : Y (Up) ")
        elif ymove == 0:
            print("Eye Postion : -Y (Down)")
        elif ymove == 2:
            print("Eye Postion : Y-Y (Constant)")
        print("\n")
        time.sleep(tm)



