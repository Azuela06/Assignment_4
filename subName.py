#I'll try to do my code last time. I kind of forgot to start with the all defs first :<<

def Statement():
    Given_name = input("First name: ")
    Last_name = input("Last name: ")
    Your_age = int(input("Age: "))
    Your_address = input("Address: ")
    return Given_name + " " + Last_name, Your_age, Your_address

def Final(Username, Age, Address):
    print(f"Hi, my name is {Username}. I am {Age} years old and I live in {Address} .")

Username, Age, Address = Statement()

Final(Username, Age, Address)


