#Inheritance
#public variable is directly used and accessible everywhere
# but private is (__) and protected is (_)

class Bank:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_balance(self,is_auth):
        if is_auth == True:
            print(self.account_number)
        else:
            print("Not Allowed")

icici = Bank(123456789012,2000)
icici.deposit(2000)
icici.check_balance()