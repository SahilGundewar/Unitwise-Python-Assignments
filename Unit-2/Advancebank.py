class bank:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}. New balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def get_account_info(self):
        return (
            f"Account Number: {self.account_number}, "
            f"Account Holder: {self.account_holder}, "
            f"Balance: {self.balance}"
        )



input_account_number = input("Enter account number: ")
input_account_holder = input("Enter account holder name: ")

account = bank(input_account_number, input_account_holder)
print("\nAccount created successfully!")

while True:
    print("\n--- Bank Menu ---")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        amount = float(input("Enter amount to withdraw: "))
        print(account.withdraw(amount))

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        print(account.deposit(amount))

    elif choice == 3:
        print(account.get_balance())

    elif choice == 4:
        print("Thank you for doing business with us!")
        break

    else:
        print("Invalid choice. Please try again.")