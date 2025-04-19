class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\n Account '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\n Account '{self.name}' balance = $ {self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount 
        print("\n Deposit Complete!")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of $ {self.balance:.2f}"
            )

    def withdrawal(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\n Withdrawal Complete! Please take your cash.")
            self.get_balance()
        except BalanceException as error:
            print(f'\n Insufficient Funds: {error}')

    def transfer (self, amount, account):
        try:
            print('\n ******* \n\n Beginning Transfer...')
            self.viable_transaction(amount)
            self.withdrawal(amount)
            account.deposit(amount)
            print('\n Transfer Complete! \n *******')
        except BalanceException as error:
            print(f'\n Transfer Interrupted!. {error}')

class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance +(amount + 1.05)
        print("\n Deposit complete.")
        self.get_balance()

class Savings(InterestRewards):
    def __init_(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\n Withdraw Complete!')
            self.get_balance()
        except BalanceException as error:
            print(f'\n Withdraw interrrupted: {error}')