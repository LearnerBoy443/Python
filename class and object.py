class account:
    def __init__(self,bal,account_number):
        self.balance=bal
        self.account_no=account_number
    def final_balance(self):
        x = input("Do you want to make changes in the account? (YES/NO): ")
        if x.upper() == "YES":
            change = input("Do you want to credit or debit? (credit/debit): ").lower()
            if change == "debit":
                debit_amount = int(input("Enter the amount to be debited: "))
                self.balance -=debit_amount
                print(f"The remaining balance is: {self.balance}")
            elif change=="credit":
                credit_amount=int(input("Enter the amt. to be credited:"))
                self.balance+= credit_amount
                print(f"The remaining balance is: {self.balance}")
            else:
                print("Invalid option chosen.")
        else:
            print(f"The balance in the account is: {self.balance}")
a1=account(10000,"X")
a1.final_balance()