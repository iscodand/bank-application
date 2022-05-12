"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo.
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. 
A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. 
Contas corrente tem um limite extra. 
Banco tem clientes e contas.
"""

# agency, account_number, balance

from bank import Bank
from account import *
from client import *


bank = Bank()

client = Client('Isco', 27)
account = CheckingAccount('banco do brasil', '123-800', 500.0)
client1 = client.insert_account(account)

bank.insert_client(client)
bank.insert_account(account)

if bank.authentication():
    print('Autenticado com sucesso!')
else:
    print('Erro na autenticação!')
