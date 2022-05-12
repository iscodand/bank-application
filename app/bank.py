class Bank():
    def __init__(self):
        self.agencys = ['111', '222', '333']
        self.clients = list()
        self.accounts = list()

    def insert_account(self, account):
        self.accounts.append(account)

    def insert_client(self, client):
        self.clients.append(client)

    def authentication(self, client):
        if client.account.agency not in self.agencys:
            return None

        if client not in self.clients:
            return None
        
        if client.account not in self.accounts:
            return None
            
        return True