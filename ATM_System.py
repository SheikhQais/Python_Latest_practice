class ATM_System:
    current_account_holders = [
        {
            "name": "Alice Johnson",
            "account_balance": 1500.75,
            "account_number": "CA1001",
            "pin": "1234",
        },
        {
            "name": "Bob Smith",
            "account_balance": 2500.50,
            "account_number": "CA1002",
            "pin": "2345",
        },
        {
            "name": "Charlie Davis",
            "account_balance": 3200.00,
            "account_number": "CA1003",
            "pin": "3456",
        },
    ]

    fast_cash_options = [20, 50, 100, 200, 500]

    def authenticate_user(self, pin_code):
        for user in self.current_account_holders:
            if user['pin'] == pin_code:
                return user
        print("Invalid PIN. Please try again.")
        return None

    def fast_cash_withdraw(self, user):
        while True:
            try:
                amount = int(input("Choose a Fast Cash option: 20, 50, 100, 200, 500 or 0 to Exit\n> "))
                if amount == 0:
                    return "Transaction cancelled."
                if amount not in self.fast_cash_options:
                    print("❌ Invalid Fast Cash option. Try again.")
                    continue
                if user['account_balance'] < amount:
                    return "Insufficient funds."
                user['account_balance'] -= amount
                return f"✅ You have successfully withdrawn ${amount} using Fast Cash option."
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def withdraw_amount(self, user):
        while True:
            try:
                amount = int(input("Enter amount to withdraw (multiples of 5) or 0 to Exit:\n> "))
                if amount == 0:
                    return "Transaction cancelled."
                if amount % 5 != 0:
                    print("❌ Please enter the amount in multiples of 5.")
                    continue
                if user['account_balance'] < amount:
                    return "Insufficient funds."
                user['account_balance'] -= amount
                return f"✅ You have successfully withdrawn ${amount}."
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def deposit_amount(self, user):
        while True:
            try:
                amount = float(input("Enter amount to deposit or 0 to Exit:\n> "))
                if amount == 0:
                    return "Transaction cancelled."
                user['account_balance'] += amount
                return f"✅ You have successfully deposited ${amount}."
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def check_balance(self, user):
        return f"💰 Your current balance is: ${user['account_balance']:.2f}"


atm = ATM_System()

user_pin = input("Enter your PIN: ")
authenticated_user = atm.authenticate_user(user_pin)

if authenticated_user:
    print(f"Welcome, {authenticated_user['name']}!")
    while True:
        user_query = input(
            "\nChoose an option:\n"
            "1. Check Balance\n"
            "2. Fast Cash Withdraw\n"
            "3. Withdraw Amount\n"
            "4. Deposit Amount\n"
            "5. Exit\n> "
        )

        if user_query == '1':
            print(atm.check_balance(authenticated_user))
        elif user_query == '2':
            print(atm.fast_cash_withdraw(authenticated_user))
        elif user_query == '3':
            print(atm.withdraw_amount(authenticated_user))
        elif user_query == '4':
            print(atm.deposit_amount(authenticated_user))
        elif user_query == '5':
            print("👋 Thank you for using our ATM!")
            break
        else:
            print("❌ Invalid option, please try again.")
else:
    print("Authentication failed.")
