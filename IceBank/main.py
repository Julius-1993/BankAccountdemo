import random
class ATM:
    BankName = "Ice Bank Plc."
    account_name = str()
    CVV = str()
    SerialNumber = int()
    ExpiryDate = "05/27"
    PIN = int()
    Type = str()

    def __init__(self, Name, Type, Pin):
        self.account_name = Name
        self.Type = Type
        self.PIN = Pin
        self.SerialNumber = random.randint(5555555555555555,9999999999999999)
        self.CVV = random.randint(000,999)

    def ATMdetails(self):
        print(f"Your Debit_Card_Details are: \n"
              f"Bank name: {self.BankName}\n"
              f"Name: {self.account_name}\n"
              f"CVV: {self.CVV}\n"
              f"Serial number: {self.SerialNumber}\n"
              f"Expiry date: {self.ExpiryDate}\n"
              f"Pin: {self.PIN}\n"
              f"Type: {self.Type}")
        print("*******************************************")


class BankAccount(ATM):
    account_name = str()
    account_number = str()
    account_balance = str()
    date_of_opening = str()
    date_of_birth = str()


    def makeATM(self,Name,type,pin):
        if self.PIN.__sizeof__() >= 4:
            print("===========================================")
            print("Welcome to Card Creation Center")
            
        elif self.PIN.__sizeof__() < 4:
            print("Welcome to Card Creation Center")
        else:
            self.PIN = pin
            print(input("Enter Your New PIN: "))


        self.ATM = ATM(Name,type,pin)
        


    def __init__( self,acct_name, date_of_opening, date_of_birth, acct_type, init_deposit):
        self.account_name=acct_name
        self.account_number=random.randint(0000000000,9999999999)
        self.account_balance=float(init_deposit)
        self.date_of_opening=date_of_opening
        self.date_of_birth=date_of_birth
        self.account_type=acct_type
        


    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        print(input("Enter name of depositor: "))
        self.account_balance += float(amount)
        print(f"₦{amount} has been deposited in your account.")
        print(f"Your available balance is: {self.account_balance}")


    def withdraw(self):
        print(input("Enter your pin: "))
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.account_balance:
            print("Insufficient balance.")
        elif amount < 0:
            print("You can't withdraw money less than zero")
        else:
            self.account_balance-=amount
            print(f"₦{amount} has been withdraw from your account.")
            print(f"Your available balance is: {self.account_balance}")

    def transfer(self):
        amount = float(input("Enter amount to transfer: "))
        print(input("Enter Recipient Account Number: "))
        print(input("Enter Recipient Bank Name: "))
        print(input("Enter your pin: "))
        if amount > self.account_balance:
            print("Insufficient balance.")
        elif amount < 0:
            print("You can't Transfer money less than zero")
        else:
            self.account_balance-=amount
            print(f"₦{amount} has been transfered from your account.")
            print(f"Your available balance is: {self.account_balance}")


    def check_balance(self):
        print(f"current balance is ₦{self.account_balance}.")


    def print_customer_details(self):
        print("Bank Name:", self.BankName)
        print("Name: ",self.account_name)
        print("Account Number:", self.account_number)
        print("Account Type: ",self.account_type)
        print("Date of birth:", self.date_of_birth)
        print("Date of opening:", self.date_of_opening)
        print(f"balance:₦{self.account_balance} \n")

# Initialization
A1 = BankAccount("David Beloved", '17-04-2023', '17-08-1995', 'Savings', 0)
A2 = BankAccount("Manji Chali", '18-04-2023', '04-09-1996', 'Current', 0)
A3 = BankAccount("Innocent Jatau", '19-04-2023', '03-12-1993', 'Savings', 0)
A4 = BankAccount("Timchit Auta", '20-04-2023', '12-01-1994', 'Current', 0)
A5 = BankAccount("Muslimat Bako", '21-04-2023', '13-04-1998', 'Savings', 0)
A6 = BankAccount("Julius Aako", '22-04-2023', '14-02-1992', 'Current', 0)
A7 = BankAccount("Tola Mapis", '23-04-2023', '25-08-1991', 'Savings', 0)

A1.makeATM("David Beloved", "Visa", 1234)
A1.ATM.ATMdetails()

A2.makeATM("Manji Chali", "Verve", 3240)
A2.ATM.ATMdetails()

A3.makeATM("Innocent Jatau", "Master", 1994)
A3.ATM.ATMdetails()

A4.makeATM("Timchit Auta", "Visa", 1994)
A4.ATM.ATMdetails()

A5.makeATM("Muslimat Bako", "Verve", 1994)
A5.ATM.ATMdetails()

A6.makeATM("Julius Aako", "Master", 1994)
A6.ATM.ATMdetails()

A7.makeATM("Tola Mapis", "Visa", 1994)
A7.ATM.ATMdetails()
print("Our Loan Application is in progress...")
