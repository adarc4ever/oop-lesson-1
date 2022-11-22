class CheckingAccount:

    def __init__(self,name,):
        self.name = name
        self.__balance = 0
        #add to balance
    def credit(self,amount):
            self.__balance += amount
        #subtract from ballance
    def debit(self, amount):
            self.__balance -= amount
        #show the balance
    def get_balance(self):
            print(f'{self.name} has {self.__balance}$ in checking account')

Jhon_Account = CheckingAccount('Jhon')
Jhon_Account.get_balance
Jhon_Account.credit(100)
Jhon_Account.get_balance()
#to direct acces
Jhon_Account.__balance = 1000000