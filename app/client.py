class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return f'Titular: {self._name}'

    @property
    def age(self):
        return f'Idade: {self._age}'


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None

    def insert_account(self, account):
        self.account = account
        return self.account
