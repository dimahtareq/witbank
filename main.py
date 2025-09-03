from BankOperations.users import Users
from BankOperations.deposit import Deposit
from BankOperations.transfer import Transfer
from BankOperations.withdrawal import Withdrawal

class Bank(Users, Deposit, Transfer, Withdrawal):

    #Deposit test:
    #try1 = Deposit("Athraa", 70000)    #We create an object to deposit.
    # try1.DepositFun()    #Now we're calling the deposit function.
    #print(Users.returnUser("Athraa"))    #See how the value changed.



    # # Transfer test:
     t=Transfer()
     t.TransferFun()
     print(Users.returnUser("Dimah"))
     print(Users.returnUser("Athraa"))


    # # Wihdrawal test:
    #try3 = Withdrawal("Athraa", 100000)
    #try3.WithdrawalFun()
    #print(Users.returnUser("Athraa"))