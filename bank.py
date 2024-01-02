

class Bank:
    
    def __init__(self,name,amount) -> None:
        self.name = name
        self.bankAmount = amount
        self.totalGivenLoan = 0
        self.adminList = []
        self.userList = []
        self.loanFeature = 1
        self.transactionHistory = []
    
