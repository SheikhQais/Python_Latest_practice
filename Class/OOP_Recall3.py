class Bank_Account:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insifficient Balance')
        self.balance -= amount
            
    def GetBalance(self):
        return self.balance
    
Person = Bank_Account(30000)
Person.deposit(15000)
print(f'Balance After Deposit: {Person.GetBalance()}')