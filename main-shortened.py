import random
'''
Snake Water Gun
snake = 1
water = -1
gun = 0

'''
computer = random.choice([1, 0, -1])
youstr = input("Enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}
you = youdict[youstr]

# By now we have two numbers(variables), you and computer 
print(f"You Choose {reversedict[you]}\nComputer Choose {reversedict[computer]}")

if(computer==you):
    print("Draw")
else:
    '''
    if(computer==1 and you==-1):
        print("You Lose!")

    elif(computer==1 and you==0):
        print("You win!")

    elif(computer==-1 and you==1):
        print("You win!")

    elif(computer==-1 and you==0):
        print("You Lose!")
    
    elif(computer==0 and you==1):
        print("You Lose!")
    
    elif(computer==0 and you==-1):
        print("You win!")
    
    else:
        print("Something went wrong")
    '''    
     # The below logic is written on the basis of the value of computer - you
    if((computer-you) == -1 or (computer-you) == 2):
       print("You Lose")

    else:
     print("You Win")
    