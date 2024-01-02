

class Admin:
    
    def __init__(self, bank, name, email, password) -> None:
        self.name = name
        self.__email = email
        self.__password = password
        self.__bank = bank
        self.__bank.adminList.append(self)



    def allTransactions(self):
        for msg in self.__bank.transactionHistory:
            print(msg)

    def allUser(self):
        for user in self.__bank.userList:
            print(user)


    def loan_off(self):
        self.__bank.loanFeature = 0

    def loan_on(self):
        self.__bank.loanFeature = 1
    
    def total_balance_of_bank(self):
        return f"Total Balance of Bank {self.__bank.bankAmount}"

    def check_loan_amount(self):
        return f"Total Loan Amount: {self.__bank.totalGivenLoan}"

    def __repr__(self) -> str:
        return f"Name:{self.name} Email:{self.__email}"

