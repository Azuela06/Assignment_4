# Note:  Still! The defs first, then make your code presentable. (tho idk how)


def Cost():
    apple = int(input("How much is the Apple: "))
    return apple

def Values():
    cashInhand = int(input("How much money you have: "))
    return cashInhand

def Max(n1,n2):
    return n1//n2

def Total(number,cost):
    return number*cost

def Change(cash,charge):
    return cash-charge

price = Cost()
print(f"Good day! To start, The apple costs {price}.")

Cash = Values()

max = Max(Cash,price)
pay = Total(max,price)

print (f"You can buy {max} apples and your change is {Change(Cash,pay)} pesos.")




    
