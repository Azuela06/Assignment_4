# redoing the program
# I am lost :<<<<

def Values():
    val1 = int(input("How much money do you have?: "))
    val2 = int(input("How much is the apple?: "))
    apple = val1//val2
    total = val2*apple
    return apple, val1-total

def Statement(Max,Change):
    print(f"You can buy {Max} apples and your change is {Change} pesos.")
    
Max_ , change = Values()

Statement(Max_, change)

