def menu():
    print("banking system")
    print("1.check balance ")
    print("2.deposit")
    print("3.withdraw")
    print("4.quit")

balance=0
while True:
    menu()
    choice=int(input("enter your choice"))
    if choice == 1:
        print("Balance:" , balance)
    elif choice == 2:
        amount = int(input("enter amount to be deposited"))
        balance += amount
    elif choice == 3:
        amount = int(input("enter amount to withdraw"))
        balance -= amount
    elif choice == 4:
        print("byee see u nxt tym")
        break
    else:
        print("invalid input please input again")


        