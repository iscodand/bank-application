# Python Object-Oriented Programming challenge.

## Tips:

- Exercise with Abstraction, Inheritance, Encapsulation and Polymorphism. Create a banking system (extremely simple) that has customers, accounts and a bank. The idea is that the customer has an account (savings or checking) and that can withdraw / deposit into that account. Checking accounts have an extra limit. Bank has customers and accounts.

- Create Customer class that inherits from the Person class (Inheritance). Person has name and age (with getters). Customer has account (Aggregation of the class ContaCorrente or ContaPoupanca).

- Create SavingAccount and CheckingAccount classes that inherit from Account. CheckingAccount must have an extra limit Accounts have branch, account number and balance Accounts must have a deposit method Account (superclass) must have the abstract withdrawal method (Abstraction and polymorphism - the subclasses that implement the withdraw method).

- Create Bank class to AGGREGATE customer and account classes (Aggregation) Bank will be responsible for authenticating the customer and the accounts as follows: Bank has accounts and customers (Aggregation) * Check if the branch is from that bank * Check if the customer is from that bank * Check if the account belongs to that bank. 

- It will only be possible to withdraw if you pass the bank authentication (described above).
