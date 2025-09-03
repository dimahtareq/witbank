from BankOperations.users import Users

class Transfer:
    def __init__(self):
        pass

    index = 0
    def accountAuthentic(self, account):     #We check to see if the account exists
        self.account = account
        for i in range(len(Users.user)):
            if(self.account.lower() == Users.user[i]['name'].lower()):
                self.index = i
                return True
        return False
    
    def TransferFun(self):

        self.index1 = 0
        self.index2 = 0
        self.name1 = input("Enter the account you want to transfer from: ").lower().strip()
        if(self.accountAuthentic(self.name1)):    #If yes, we check the second account
            self.index1 = self.index
            self.name2 = input("Enter the account you want to transfer to: ").lower().strip()
            if(self.accountAuthentic(self.name2)):
                self.index2 = self.index
                self.amountTransfered = int(input("Enter the amount you want to transfer: "))
                if(self.amountTransfered <= 0):
                    print("Please enter a valid value!")
                    return
                if(Users.user[self.index1]['credit'] >= self.amountTransfered):
                    Users.user[self.index1]['credit'] -= self.amountTransfered
                    Users.user[self.index2]['credit'] += self.amountTransfered
                    print(f"Transfer is done successfully!. Your account {self.name1} now has only {Users.user[self.index1]['credit']}.")
            else:
                print("There is no such account to transfer to!")
                return
        else:
            print("There is no such account to transfer from!")
            return