import re
DEBUG=True

class Category:
    ledger=list()
    balance=0

    def __init__(self, categories):
        self.categories = categories.capitalize()
        if DEBUG:
            print(self.categories)
        
    def __str__(self):
        lencat=len(self.categories)
        output=""
        for i in range (int((30-lencat)/2)):
            output=output+"*"
        output=output+self.categories
        for i in range (int((30-lencat)/2)):
            output=output+"*"
        if DEBUG:
            print(str(self.ledger[0]))
            print(''.join(re.findall("-?([^\s]+)?",str(self.ledger[0]))))
        return output

    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
        if DEBUG:
            print(self.ledger)
        self.balance=self.balance+amount
        return

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            amount=amount*(-1)
            self.ledger.append({"amount": amount, "description": description})
            self.balance=self.balance+amount
            if DEBUG:
                print(amount)
            return True
        else: return False

    def get_balance(self):
        return self.balance

    def transfer(self,amount,other):
        if DEBUG:
            print(other.categories)
        description="Transfer to "+other.categories
        if self.withdraw(amount,description):
            description="Transfer from "+self.categories
            other.deposit(amount, description)
            return True
        else: return False

    def check_funds(self, amount):
        if int(amount)>int(self.get_balance()):
            return False
        else: return True

def create_spend_chart(categories):
    return 