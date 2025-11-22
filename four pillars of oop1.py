class ATM:
    def __init__(self,balance):
        self.__balance = balance #private attribute 

    def deposit (self,amount):
        self.__balance += amount
        print(f"deposited:{amount} . new balance:{self.__balance}")

    def withdraw (self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw{amount} . new balance:{self.__balance}")
        else:
            print("insufficient balance")

atm=ATM(1000)
atm.deposit(500)
atm.withdraw(300)


'''in this above code i cant change the balance directly bcz i used self.__balance
if i use only self.balance anyone can change the balance directly
soo this self.__balance we call as private attribute bcz only i can change the balance and not others '''


class ATM:
    def __init__(self,balance):
        self.balance = balance

    def deposit (self,amount):
        self.balance += amount
        print(f"deposited:{amount} . new balance:{self.balance}")

    def withdraw (self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdraw{amount} . new balance:{self.balance}")
        else:
            print("insufficient balance")

atm=ATM(1000)
atm.deposit(500)
atm.withdraw(300)