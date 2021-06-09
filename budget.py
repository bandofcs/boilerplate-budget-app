import re
DEBUG=False

class Category:

    def __init__(self, categories):
        self.categories = categories.capitalize()
        self.balance=0
        self.ledger=list()
        self.spent=0
        if DEBUG:
            print(self.categories)
        
    def __str__(self):
        lencat=len(self.categories)
        output=""
        line=""
        for i in range (int((30-lencat)/2)):
            output=output+"*"
        output=output+self.categories
        for i in range (int((30-lencat)/2)):
            output=output+"*"
        output=output+"\n"
        if DEBUG:
            print(str(self.ledger[0]))
        for i in range(len(self.ledger)):
            amount=(str(self.ledger[i])).split(",")[0].split(" ")[1]
            if amount.count(".")==0:
                amount=amount+".00"
            description=(str(self.ledger[i])).split(",")[1].split(": '")[1].rstrip("'}")
            j=0
            while j<23:
                if j<len(description):
                    line=line+description[j]
                else:
                    line=line+" "
                j=j+1
            while j<(30-len(amount)):
                line=line+" "
                j=j+1
            line=line+amount
            line=line+"\n"
            if DEBUG:
                print(output+line)
        return output+line+"Total: "+ str(self.get_balance())

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
            self.spent=self.spent-amount
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

def create_spend_chart(listofcategories):
    total=0.00
    i=0
    for i in range(int(len(listofcategories))):
        total=total+listofcategories[i].spent
        print(format(total,'.2f'))
    return 