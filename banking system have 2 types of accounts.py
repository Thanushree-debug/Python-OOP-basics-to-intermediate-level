class account:
    def __init__(self,id,holder_name):
       self.id=id
       self.holder_name=holder_name
       self._balance=0 #encapsulation #protected attribute not private 

    def check_balance(self):
       print("balance: {self._balance}")

    def deposit(self, amount):
       self._balance += amount
       print(f"deposit successful . updated balance = {self._balance}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
           self._balance -= amount
           print("withdraw successful, updated balance={self._balance}")
        else:
           print("no sufficient balance")

class savingsaccount(account):#inheritance
    def calculate_interest(self):
        interest_rate = 0.04 #4%
        interest = self._balance * interest_rate 
        print(f"interest:{interest}")

class currentaccount(account):
    def withdraw(self,amount):#polymorphism
        over_draft_limit = 1000
        if self._balance + over_draft_limit >= amount:
            self._balance -= amount
            print(f"withdraw successful, updated balance={self._balance}")
        else:
            print("amount asked is more than over draft limit")

class bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__accounts = {}

    def create_acc(self,id,holder_name,type):
        if type=="savings":
            new_acc = savingsaccount(id,holder_name)
        elif type == "current":
            new_acc = currentaccount(id,holder_name)
        self.__accounts[id] = new_acc
        print("acc creation successful")
        return new_acc
    
    def get_account(self,id):
        if id not in self.__accounts:
            print("acc not found")
            return None
        else:
            account = self.__accounts[id]
            print(f"\n id: {account.id}\n holder_name: {account.holder_name}")
            return account
        
cbk = bank("chandan bank of karnataka" , "mysore")
s_a1=cbk.create_acc("1" , "darshan" , "savings")
c_a1=cbk.create_acc("2" , "viraj" , "current")

s_a1.deposit(1000)
c_a1.deposit(10)

s_a1.withdraw(2000)
c_a1.withdraw(200)

s_a1.calculate_interest()