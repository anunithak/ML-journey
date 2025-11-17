class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return self.length* self.width
    
    def perimeter(self):
        return 2* (self.length+self.width)
    

class BankAccount:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount},new balance={self.balance}")
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrew {amount}, new balance={self.balance}")
        else:
            print("Not enough balance!")
    
    def get_balance(self):
        return self.balance



to_check=rectangle(30,60)
print(to_check.area())
print(to_check.perimeter())

bank=BankAccount(100)
bank.deposit(500)
bank.withdraw(400)
print(bank.get_balance)