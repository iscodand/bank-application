## Python Object-Oriented Programming challenge.

# In the "SOLUÇÃO" folder there's the teachers soluction the following challenge:

# Tips:

- Create Customer class that inherits from the Person class (Inheritance) Person has name and age (with getters) Customer TEM account (Aggregation of the class ContaCorrente or ContaPoupanca) 

- Create ContaPoupanca and ContaCurrente classes that inherit from Conta Current Account must have an extra limit Accounts have branch, account number and balance Accounts must have a deposit method Conta (super class) must have the abstract withdrawal method (Abstraction and polymorphism - the subclasses that implement the withdraw method) 

- Create Bank class to AGGREGATE customer and account classes (Aggregation) Bank will be responsible for authenticating the customer and the accounts as follows: Bank has accounts and customers (Aggregation) * Check if the branch is from that bank * Check if the customer is from that bank * Check if the account belongs to that bank 

- It will only be possible to withdraw if you pass the bank authentication (described above)
