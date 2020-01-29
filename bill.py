name=input("enter your name")
board=input("enter your boarding place")
dest=input("enter your destination place")
km=int(input("enter number of kilometers"))
date=input("enter date of journey")
faci=int(input("enter facility \n 1.normal \n 2.delux \n 3.super fast \n 4.ultra delux "))
price=0
if faci==1 :
    price=km*6
  #  print(price)
elif faci==2 :
    price=km*8
    #print(price)
elif faci==3 :
    price=km*12
 #   print(price)
elif faci==4 :
    price=km*15
  #  print(price)
else:
    print("enter correct option")
print("name:",name)
print("source:",board)
print("destination:",dest)
print("date of journey:",date)
print("distance:",km)
print("total price:" ,price)
