class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", self.balance)

    def display(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


account1 = Bank("Shins", 1000)

account1.display()
account1.deposit(500)
account1.withdraw(2000)
account1.display()


    
        


