class Account():
    def __init__(self, agency, account_number, balance):
        self.agency = agency.title()
        self._account_number = account_number
        self._balance = balance
        self._limit = 1000.0

    def __withdraw_disponible(self, value):
        self.total_limit = self._limit + self._balance
        return value <= self.total_limit

    def deposit_money(self, value):
        print(f'Você depositou R$ {value}')
        self._balance += value

    def withdraw_money(self, value):
        if (self.__withdraw_disponible(value)):
            self._balance -= value
            print(f'Você sacou R$ {value}')
        else:
            print('Saldo/Limite Insuficiente!')

    def transfer_money(self, value, destiny_account):
        if (self.__withdraw_disponible(value)):
            self.withdraw_money(value)
            destiny_account.deposit_money(value)
            print(f'Você transferiu R$ {value}')
        else:
            print('Transação não aceita!')

    @property
    def account_number(self):
        return f'Conta: {self._account_number}'

    @property
    def balance(self):
        return f'Saldo: R$ {self._balance}'

    @property
    def limit(self):
        return f'Limite: R$ {self._limit}'


class SavingsAccount(Account):
    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)


class CheckingAccount(Account):
    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)
        self._limit += 500
