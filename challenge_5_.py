# Handling a Bank Account


class Account:
    def __init__(self):
        self.balance = 0
        print("The Account is created")

    def deposit(self,amount):
        amount = float(input("enter the amount to be deposit : "))
        self.balance = self.balance + amount
        print("Deposit is successful and the balance in the account is : ",self.balance )

    def withdrawal(self,amount):
        amount = float(input("enter the amount to be withdrawal : "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print ("The withdrawal is successfull and balance id : ",self.balance)
        else:
            print("insuficient fund ")


    def getBalance(self):
        print("Balance in the account is %f"% self.balance)


class SavingAccount(Account):
    def _init_(self,balance,interest_rate):
        super()._init_(balance)
        self.interest_rate = interest_rate

    def interestrate(self,interest_rate,p=0,t=0,r=0):
        p = float(input("enter the balance in account :"))
        t = int(input("enter the time period to keep :"))
        r = float(input("enter the interestrate :"))
        print("The principle amount is :",p)
        print("The time period in year is :", t)
        print("The rate of interest : ",r)

        interest_rate = (p * t * r)/100
        print("interestamount is :",interest_rate)
        pass
Account_obj = Account()
Account_obj.deposit(1) 
Account_obj.withdrawal(1)
Account_obj.getBalance()
SavingAccount_obj=SavingAccount(balance=0,interest_rate=0)
SavingAccount_obj.interest_rate(1)
