class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self._balence += amount  # Protected attribute
        print(f"Deposited {amount}. New balance is {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456", 1000)
account.deposit(500)
print(account.get_balance())