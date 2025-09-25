class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
        
    def deposit(self,amount):
       if amount>0:
           self.__balance+=amount
           print(f'deposited {amount}')
       else:
           print('deposit amount must be positive')
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f'withdraw {amount}')
        else:
            print('invalid balance')
    def checkbalance(self):
        return self.__balance
acc=BankAccount(500)
acc.deposit(200)
acc.withdraw(100)
print('balance:',acc.checkbalance())
