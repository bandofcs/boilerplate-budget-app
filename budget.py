import math
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
            description=(str(self.ledger[i])).lstrip(", ").split(": '")[1].rstrip("'}")
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
        else: 
            return False

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
        if amount>self.get_balance():
            return False
        else: return True

def create_spend_chart(listofcategories):
    percentagechart = ["","","","","","","","","","",""]

    total=0.00
    i=0
    percentagelist=list()
    longestcategory=0
    label=""
    for i in range(len(listofcategories)):
        total=total+listofcategories[i].spent
    i=0
    for i in range(len(listofcategories)):
        percentagelist.append(int(math.floor(listofcategories[i].spent/total*10.0))*10)
        if len(listofcategories[i].categories)>longestcategory:
            longestcategory=len(listofcategories[i].categories)

    #Popular the bar chart
    i=0
    percentage=100
    for i in range(len(percentagechart)):
        j=0
        for j in range(len(listofcategories)):
            if percentage<=percentagelist[j]:
                percentagechart[i]=percentagechart[i]+"o  "
            else:
                percentagechart[i]=percentagechart[i]+"   "
        percentage=percentage-10
    #print the bar chart
    barchart="100| "+percentagechart[0]+"\n"\
    +" 90| "+percentagechart[1]+"\n"\
    +" 80| "+percentagechart[2]+"\n"\
    +" 70| "+percentagechart[3]+"\n"\
    +" 60| "+percentagechart[4]+"\n"\
    +" 50| "+percentagechart[5]+"\n"\
    +" 40| "+percentagechart[6]+"\n"\
    +" 30| "+percentagechart[7]+"\n"\
    +" 20| "+percentagechart[8]+"\n"\
    +" 10| "+percentagechart[9]+"\n"\
    +"  0| "+percentagechart[10]+"\n"

    #print the line
    j=0
    line="    "
    for j in range(len(listofcategories)):
        line=line+"---"
    line=line+"-\n"
    #print the label
    i=0
    j=0
    #for each row
    for i in range(longestcategory):
        if i>0:
            label=label+"\n"
        label=label+"     "
        #for each category
        for j in range(len(listofcategories)):
            #for each letter in category
            if i<len(listofcategories[j].categories):
                label=label+listofcategories[j].categories[i]+"  "
            else:
                label=label+"   "
        
    return "Percentage spent by category\n"+barchart+line+label