from BankOperations.users import Users
class Withdrawal:
    def __init__(self, name, amountWithdrawn):
        self.name = name
        self.amountWithdrawn = amountWithdrawn
    
    def WithdrawalFun(self):
        if(self.amountWithdrawn <= 0):
            print("Please enter a valid value!")
            return
        
        for i in Users.user:
            if (self.name.lower()== i['name'].lower()):
                if (i['credit'] >= self.amountWithdrawn):    #"name" can't withdraw if the amount withdrawn is bigger than their credit.
                    i['credit'] -= self.amountWithdrawn
                    print(f"Withdrawal is done successfully!. Your account {i['name']} now has {i['credit']}")
                    return
                else:
                    print("Sorry, you don't have enough credit to withdraw from your account!")
                    return
        print("There is no such user to withdraw from!")   #The loop won't return if there is no such user
        return