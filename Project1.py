import random
def swg(choice):
    dict = {"s":1 , "w":0, "g":-1}
    comp = random.randint(-1,1)
    your = dict[choice]
    if(your == comp):
        print("It's a Tie")
        return 
    else:
        if(your == 1 and comp == 0):
            print("You win")
            return
        elif(your == 0 and comp == -1):
            print("You win")
            return
        elif(your == -1 and comp == 1): 
            print("You win")
            return
        else:
            print("You lose")
            return

a = input('''Enter your choice
          s : Snake
          w : Water
          g : Gun\n''')
swg(a)
