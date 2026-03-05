class BankAccount:

    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Amount Deposited Successfully")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:",self.balance)


class Bank:

    def __init__(self):
        self.accounts={}

    def create_account(self,name,acc_no,balance):
        self.accounts[acc_no]=BankAccount(name,acc_no,balance)
        print("Account Created Successfully")

    def deposit_money(self,acc_no,amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account Not Found")

    def withdraw_money(self,acc_no,amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account Not Found")

    def show_balance(self,acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].show_balance()
        else:
            print("Account Not Found")


bank=Bank()

while True:

    print("\n1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        name=input("Enter name: ")
        acc_no=int(input("Enter account number: "))
        balance=int(input("Enter initial balance: "))
        bank.create_account(name,acc_no,balance)

    elif choice==2:
        acc_no=int(input("Enter account number: "))
        amount=int(input("Enter amount: "))
        bank.deposit_money(acc_no,amount)

    elif choice==3:
        acc_no=int(input("Enter account number: "))
        amount=int(input("Enter amount: "))
        bank.withdraw_money(acc_no,amount)

    elif choice==4:
        acc_no=int(input("Enter account number: "))
        bank.show_balance(acc_no)

    elif choice==5:
        print("Thank You")
        break