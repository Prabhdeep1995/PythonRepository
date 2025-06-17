# BankDetails, CustomerDetails → Account use multiple inheritance
# BankDetails: bank_name, branch
# CustomerDetails: customer_name, aadhar_number
# Account: account_number, balance
# Inherit from both and display full account info.

class BankDetails:
    def __init__(self, bank_name, branch):
        self.bank_name = bank_name
        self.branch = branch

class CustomerDetails:
    def __init__(self,customer_name, aadhar_number):
        self.customer_name = customer_name
        self.aadhar_number = aadhar_number

class Account(BankDetails,CustomerDetails):
    def __init__(self,bank_name, branch, customer_name, aadhar_number, account_number, balance):
        BankDetails.__init__(self,bank_name,branch)
        CustomerDetails.__init__(self, customer_name,aadhar_number)
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"The bank name is {self.bank_name} and the branch name is {self.branch}")
        print(f"The customer name is {self.customer_name} and his Aadhar number is {self.aadhar_number}")
        print(f"The account number is {self.account_number} and balance is {self.balance}")

account1 = Account('SBI','Noida','Rahul','56453477564','76455687',87657)
account1.display()