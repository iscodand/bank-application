from client import *


class Account():
    def __init__(self, agency, account_number, balance):
        self.agency = agency
        self._account_number = account_number
        self._balance = balance
        self._limit = 1000.0

    def __withdraw_disponible(self, value):
        self.total_limit = self._limit + self._balance
        return value <= self.total_limit

    def deposit_money(self, value):
        self._balance += value

    def withdraw_money(self, value):
        if (self.__withdraw_disponible(value)):
            self._balance -= value
        else:
            print('Saldo/Limite Indisponível!')

    def transfer_money(self, value, destiny_account):
        
        destiny_account.deposit_money(value)

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def limit(self):
        return self._limit


class SavingsAccount(Account):
    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)
        self


class CheckingAccount(Account):
    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)
        self._limit += 500


##### TEST ZONE #####

conta1 = SavingsAccount('BB', 123, 500.0)
conta2 = CheckingAccount('BB', 123, 250.0)

conta2.transfer_money(2000.0, conta1)

print(conta1.balance)

