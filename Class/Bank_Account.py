class Account:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        else:
            print('Insufficient balance.')

    def __str__(self):
        return f'Account Holder: {self.holder_name}, Balance: {self.balance}'


class SavingsAccount(Account):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate  # as a percentage

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f'Interest applied: {interest}. New balance: {self.balance}')


class CheckingAccount(Account):
    def __init__(self, holder_name, balance, overdraft_limit):
        super().__init__(holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        else:
            print('Overdraft limit exceeded.')


# --- Example Usage ---

# Savings Account
savings = SavingsAccount('Ali', 10000, 5)
print(savings)
savings.apply_interest()
savings.withdraw(2000)
savings.deposit(1500)
print()

# Checking Account
checking = CheckingAccount('Waleed', 5000, 2000)
print(checking)
checking.withdraw(6000)   # Should succeed (overdraft allowed)
checking.withdraw(2000)   # Should fail (overdraft limit exceeded)
checking.deposit(1000)