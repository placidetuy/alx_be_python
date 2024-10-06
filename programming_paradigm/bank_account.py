class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Deduct the amount if there are sufficient funds."""
        if amount > self.account_balance:
            return False  # Insufficient funds
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")

