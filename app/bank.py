from account import *
from client import *


class Bank(Account, Client):
    def __init__(self):
        self.client = None
        self.account = None

    def insert_client(self, client):
        self.client = client
        return self.client

    def insert_account(self, account):
        self.account = account
        return self.account

    def authentication(self):
        if self.agency == 'Banco Do Brasil' and self.account_number.startwith('123'):
            return f'Bem-vindo {self._name}!'
        else:
            return f'Conta não autenticada!'