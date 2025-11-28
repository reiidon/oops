class Bank:

    def init (self, balance=0):

        self.balance = balance
        self.rate = 0.02 

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount

        else:
            print("not enough balance")

    def get_balance(self):
        return self.balance

    def get_interest(self):
        return self.balance*self.rate