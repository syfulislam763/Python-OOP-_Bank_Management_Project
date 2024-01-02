from bank import Bank
from admin import Admin
from user import User



def main():
    PeopleBank = Bank("People Bank", 1)
    #create admin account to people bank
    admin = Admin(PeopleBank,"shariful islam", "shariful@gmail.com","123")
    #create user account to people bank
    user1 = User(PeopleBank,"hydar mia", "hydar@gmail.com", "1234")
    user2 = User(PeopleBank, "karim", "karim@gmail.com", "3232")
    user3 = User(PeopleBank,"aftab khan", "aftab@gamil.com", "2324")
    user4 = User(PeopleBank, "akib rahat", "akib@gmail.com", "3732")
    user5 = User(PeopleBank,"asraf ali", "asraf@gamil.com", "2394")

    #deposit
    deposit = user1.deposit(1000)
    print(deposit)
    deposit = user2.deposit(9000)
    print(deposit)

    total_bank_amount = admin.total_balance_of_bank()
    print(total_bank_amount)

    deposit = user3.deposit(3000)
    print(deposit)
    deposit = user4.deposit(7000)
    print(deposit)
    deposit = user5.deposit(4000)
    print(deposit)
    
    total_bank_amount = admin.total_balance_of_bank()
    print(total_bank_amount)
    
    #withdraw
    
    withdraw = user2.withdraw(4000)
    print(withdraw)
    withdraw = user1.withdraw(2000)
    print(withdraw)
    withdraw = user4.withdraw(1000)
    print(withdraw)

    total_bank_amount = admin.total_balance_of_bank()
    print(total_bank_amount)

    deposit = user2.deposit(2000)
    print(deposit)

    total_bank_amount = admin.total_balance_of_bank()
    print(total_bank_amount)

    #loan funtionality
    take_loan = user2.take_loan(4000)
    print(take_loan)
    take_loan = user1.take_loan(4000)
    print(take_loan)
    take_loan = user4.take_loan(10000)
    print(take_loan)

    admin.loan_off()

    take_loan = user5.take_loan(8000)
    print(take_loan)

    admin.loan_on()

    take_loan = user5.take_loan(8000)
    print(take_loan)
    take_loan = user5.take_loan(2000)
    print(take_loan)
    
    total_loan_amount = admin.check_loan_amount()
    print(total_loan_amount)
    
    total_bank_amount = admin.total_balance_of_bank()
    print(total_bank_amount)


    user_balance = user1.check_balance()
    print(user_balance)
    user_balance = user2.check_balance()
    print(user_balance)

    transaction = user2.transfer_amount("karim@gmail.com", "3232", "hydar@gmail.com", 5000)
    print(transaction)

    transaction = user1.transfer_amount("hydar@gmail.com", "1234", "karim@gmail.com", 2000)
    print(transaction)

    user1.check_transaction_history()
    user2.check_transaction_history()

    user_balance = user1.check_balance()
    print(user_balance)
    user_balance = user2.check_balance()
    print(user_balance)


    #admin.allTransactions()
    

    # print("Users of people bank:")
    # admin.allUser()





if __name__ == "__main__":
    main()
