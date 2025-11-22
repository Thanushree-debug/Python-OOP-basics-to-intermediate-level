def menu():
    print("banking system")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.quit")
balance=0

while True:
    menu()
    choice = int(input("enter ur choice"))
    if choice == 1:
        print("balance:", balance)
    if choice == 2:
        amount = int(input("enter amount to deposit"))
        balance += amount
    if choice == 3:
        amount = int(input("enter amount to withdraw"))
        balance -= amount
    else:
        print("quit")

    



