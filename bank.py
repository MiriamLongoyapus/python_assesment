# Add these attributes and behaviors to the class Account
# Add attributes deposits and withdrawals in the init method
# which are empty lists by default and another attribute loan_balance
#  which is zero by default.
class Account:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
# Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return self.balance
# Update the deposit method to append each withdrawal transaction
# to the deposits list. Each transaction should be in form
# of a dictionary like this
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    def deposit(self, amount):
        self.balance += amount
        transaction_of_deposit = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction_of_deposit)
# Update the withdrawal method to append each withdrawal transaction to the withdrawals list.
#  Each transaction should be in form of a dictionary like like this
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    def withdrawal(self, amount):
        if self.balance < amount:
            return "You have {amount} shillings and Remaining balance is {self.balance} shillings"
        else:
            self.balance -= amount
            withdrawal = {
                "amount": amount,
                "narration": "withdrawal"
            }
            self.withdrawals.append(withdrawal)
# Add a new method  print_statement which combines both deposits and withdrawals into one list and,
# using a for loop, prints each transaction in a new line like this deposit - 1000withdrawal - 500
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            narration = transaction["narration"]
            amount = transaction["amount"]
            print(narration, "-", amount)
# Add a borrow_loan method which allows acustomer to borrow if they meet these conditions:
# Account has no outstanding loan Loan amount requested is more than 100
# Customer has made at least 10 deposits.Amount requested is less than or equal to 1/3
# of their total sum of all deposits.A successful loan increases the loan_balance by requested amount
    def loan_borrowed(self, amount):
        if self.loan_balance == 0 and len(self.deposits) > 10 and amount > 100 and amount <= (1/3 * sum(self.deposits)):
            self.loan_balance += amount
            self.balance += amount
            return "Loan approved"
        else:
            return "Loan not approved"
# Add a repay_loan method with this functionalityA customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            return "loan fully repaid your loan balance is 0"
        else:
            self.loan_balance -= amount
            self.balance += amount
            return "you have paid a loan of {self.amount} and your loan balance is {self.balance}"
# Add a transfer method which acceptstwo attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested amount from
# the current account to the passed account. The transfer isaccomplished by reducing the current account balance
#  and depositing the requested amount to the passed account.
    def transfer(self, amount, account):
        if self.balance >= amount:
            self.balance -= amount
            account.deposit(amount)
            return "Transfer was successful and your balance is {self.balance} shillings"
        else:
            return "Insufficient funds for transfer balance is {sel.balance} shillings"
