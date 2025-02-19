# class bank
# method1 : name,ac_type,balance
# method2 : amt_deposit
# method3 : amt_withdraw
# method3 : show_balance

# random module                                             # this module is using to generate random number for account number or password

class Bank:

    def __init__(self,name,ac_type,balance):

        self.name = name

        self.balance = balance

    def amount_deposit(self,amount):                        # ammount depositing

        self.balance = self.balance + amount

        print(f"Amount deposited successfully")

        print(f"Avalilable balance is {self.balance}")

    def amount_withdrawal(self,amount):                     # amount withdrawing

        if amount < self.balance:

            self.balance = self.balance - amount

            print(f"Amount withdrawal successfull")

            print(f"Available balance is {self.balance}")

        else:

            print("Insufficient Balance")

    def show_balance(self):                                 # avalilable balance

        print(f"Account Holdername : {self.name}")

        print(f"Account Balance    : {self.balance}")

obj1 = Bank(name="adarsh",ac_type="savings",balance=4000)

obj1.amount_deposit(2000)

obj1.amount_withdrawal(200)

obj1.show_balance()