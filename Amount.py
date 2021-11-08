# Note: def function should always comes first
# Please read this before you pass this :>>>

def Payables():
    orange = int(25)
    apple = int(20)
    Apple_ = int(input("Number of apples you want: "))
    Orange_ = int(input("Number of oranges you want: "))
    return (apple*Apple_),(orange*Orange_)

def Total (Apple,Orange):
    return Apple+Orange

appleTotal, orangeTotal = Payables()

print (f"The total amount is {Total(appleTotal,orangeTotal):.2f}.")



