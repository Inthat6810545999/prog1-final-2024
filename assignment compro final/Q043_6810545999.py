# Name: Inthat # Student ID: 68010545999
from re import split


class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner 
        self.__balance = balance

    def get_balance(self):
        return f'{(self.__balance):.2f}'
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            return False


while True:
    owner = input("Enter account owner: ")
    b = float(input('Enter initial balance: '))
    print(f'Welcome, {owner}.')
    owner = BankAccount(owner, b)
    com = input("Enter command: ")
    if com.lower() == 'exit':
        print("Goodbye.")
        break
    elif 'deposit' in com.lower():
        try:
            splitter = com.split()
            if float(splitter[-1]) >= 0:
                owner.deposit(float(splitter[-1]))
                print(f"Deposit successful. New balance: {(owner.get_balance())}")
            else:
                print(f'Insufficient funds or invalid amount.')
        except:
            print("Insufficient funds or invalid amount.")
    elif 'withdraw' in com.lower():
        try:
            splitter2 = com.split()
            if float(splitter2[-1]) >= 0:
                owner.withdraw(float(splitter2[-1]))
                print(f"Withdraw successful. New balance: {(owner.get_balance())}")
        except:
            print(f'Insufficient funds or invalid amount.')
    else:
        print('Insufficient funds or invalid amount.')

