import random
n=random.randrange(0,50)
for i in range(3):
    a=int(input("enter a value"))
    if n==a:
        print("you won")
        break
    else:
        if i==3:
            print('you loose')
            
        else:
            print("try again")
        continue
    
