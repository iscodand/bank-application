"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from bank import Bank
from account import *
from client import *


# Definindo a Variável para o Banco
bank = Bank()

# Criando os clientes e suas respectivas contas
client1 = Client('Isco', 27)
account1 = CheckingAccount('111', '123-700', 500.0)
client1.insert_account(account1)

client2 = Client('Guilherme', 30)
# Nesse caso, a agência do 'Guilherme' não é válida, pois não consta nas agências do Banco
account2 = CheckingAccount('444', '123-900', 500.0)
client2.insert_account(account2)

# Fazendo o 'login' no banco com as contas
bank.insert_client(client1)
bank.insert_account(account1)

bank.insert_client(client2)
bank.insert_account(account2)

# Ao autenticar o 'cliente 1', você verá que tudo ocorrerá perfeitamente, podendo realizar todas as 'ações bancárias'
if bank.authentication(client1):
    print(f'Olá {client1.name}. Você foi Autenticado com sucesso!')
    print(client1.name)
    client1.account.withdraw_money(30.0)
    print(client1.account.balance)
    print(client1.account.limit)
else:
    print('Falha na autenticação!')

print('-='*30)

# O 'cliente 2' não será autenticado, logo não poderá usufruir das funcionalidades bancárias
if bank.authentication(client2):
    print(f'Olá {client2.name}. Você foi Autenticado com sucesso!')
    print(client2.name)
    client2.account.withdraw_money(30.0)
    print(client2.account.balance)
    print(client2.account.limit)
    print(client2.name)
else:
    print('Falha na autenticação!')
