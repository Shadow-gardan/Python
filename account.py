class account:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def debit(self, amount):
        if amount > 0:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}.")
        else:
            print("Debit amount ")

    def credit(self, amount):
        if 0 < amount <= self.balance:
            self.balance += amount
            print(f"Credited {amount}. New balance is {self.balance}.")
        else:
            print("Credit amount")\

    def get_balance(self):
        return self.balance     
    
s1 = account("s1", 1000)
s1.debit(100)
s1.credit(200)  
print(s1.get_balance())  # Output: 1100
s1.debit(1200)  # Attempt to debit more than balance        