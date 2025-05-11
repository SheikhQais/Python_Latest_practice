class Account:
    def __init__(self, holder_name, balance):
        self.Holder_Name = holder_name
        self.Balance = balance
        
    def __str__(self):
        return f'Account Holder\'s Name: {self.Holder_Name} \nAvailable Balance: {self.Balance}'
        
    def Deposit(self, Deposit_Amount):
        self.Balance += Deposit_Amount
        print(f'New Balance: {self.Balance}')
        
    def Withdraw(self, Withdraw_Amount):
        if Withdraw_Amount <= self.Balance:
            self.Balance -= Withdraw_Amount
            print(f'New Balance: {self.Balance}')
        else:
            print('Insufficient balance')

class Interest(Account):
    def __init__(self, holder_name, balance, interest):
        super().__init__(holder_name, balance)
        self._interest = interest
        
    def Interest(self):
        profit = self.Balance * (self._interest * 0.01)
        print(f'Every year you will get {profit} on your saving account')

# Test
Acc = Interest('Qais', 50000, 6)
print(Acc)  # Now this will show account info
Acc.Deposit(60000000)
Acc.Withdraw(90000000)
Acc.Interest()