from BankOperations.users import Users

class Deposit:
    def __init__(self, name, amountAfter):
        self.name = name
        self.amountAfter = amountAfter

    def DepositFun(self):
        if (self.amountAfter > 0):
            for i in Users.user:
                if (self.name.lower() == i['name'].lower()):
                    i['credit'] += self.amountAfter
                    print(f"Deposit is done successfully!. Your account {i['name']} now has {i['credit']}.")
                    return
            print("There is no such user to deposit to!")
            return
        else:
            print("Please enter a valid value!")