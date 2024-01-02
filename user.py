

from datetime import datetime


class User:
    def __init__(self,bank, name, email, password) -> None:
        self.name = name
        self.email = email
        self.__password = password
        self.availableBalance = 0
        self.transaction = []
        self.__loan = 0
        self.__bank = bank
        self.__bank.userList.append(self)


    def take_loan(self, amount):
        if(self.__bank.loanFeature==0):
            return f"Username: {self.email}, Message: Bank is not allowing loan at this moment!"
        if amount < 1:
            return f"Username: {self.email}, Message: Request is invalid!"

        if(amount>self.availableBalance*2):
            return f"Username: {self.email}, Message: amount exceeded loan limit of {self.availableBalance*2}!"
        
        if(amount>self.__bank.bankAmount):
            return f"Username: {self.email}, Message: Bank has not sufficient balance"

        self.__bank.bankAmount -= amount
        self.__bank.totalGivenLoan += amount
        self.__loan += amount

        return f"Username: {self.email}, Message: You got loan {amount}! and Current total loan is {self.__loan}"


    
    def check_transaction_history(self):
        print(f"Transaction History of {self.name}: ")
        for h in self.transaction:
            print(h)
    
  
    def transfer_amount(self,email, password, receiver, amount):
        if( amount < 1):
            return f"Username: {self.email}, Message: Ivalid amount"
        if(amount>self.availableBalance):
            return f"Username: {self.email}, Message: You do not have sufficient balance!"
        if(self.email==email and self.__password==password):
            container = []
            
            for person in self.__bank.userList:
                if person.email == receiver:
                    container.append(person)

            if(len(container)<=0):
                return f"Username: {self.email}, Message: From {email} to {receiver} transaction failed!"

            container[0].availableBalance += amount
            self.availableBalance -= amount
            
            sender = f"Name: {self.name}, Email: {self.email}, Type: sent, To: {receiver}, Amount:{amount}, Time: {datetime.now()}"
            to = f"Name: {container[0].name}, Email: {receiver} Type: received, From: {self.email}, Amount: {amount}, Time: {datetime.now()}"

            self.transaction.append(sender)
            container[0].transaction.append(to)
            self.__bank.transactionHistory.append(sender)
            self.__bank.transactionHistory.append(to)
            return sender
        else:
            return f"Username: {self.email}, Message: Your username or password not matching!"

    def check_balance(self):
        return f"Username: {self.email}, Current balance: {self.availableBalance}"
    
    def deposit(self, amount):
        if(amount<0):
            return f"Username: {self.email}, Message: {amount} is not valid"
        self.availableBalance += amount
        self.__bank.bankAmount += amount
        return f"Username: {self.email}, Deposited:{amount}, Current balance: {self.availableBalance}"

    def withdraw(self, amount):
        if(amount<0):
            return f"Username: {self.email}, Message: {amount} is not valid"
        if(amount>self.availableBalance):
            return f"Username: {self.email}, Message: Your balance is less than {amount}"

        self.availableBalance-=amount
        self.__bank.bankAmount -= amount
        return f"Username: {self.email}, Withdrawn:{amount}, Currnet balance:{self.availableBalance}"



    def __repr__(self):
        return f"Name: {self.name}, Bank Name: {self.__bank.name}, Available balance: {self.availableBalance}, Loan: {self.__loan}"


    
