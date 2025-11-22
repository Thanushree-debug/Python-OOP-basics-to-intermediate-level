class bankacc:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance<amount:
            print("insufficient balance")
            return #if  i dont give this return statement, it will show both insuffcient balance and withdraw successful-balance: -800.
                   # so we dont want this to happen that is the only reason we will give return statement. of i give return it will show only insufficient balance 
            
        self.__balance -= amount
        print(f"withdraw successful-balance:{self.__balance}")

a=bankacc(acc_no=123 , balance=100)
a.check_balance()
a.deposit(100)
a.check_balance()
a.withdraw(1000)
a.check_balance



    
