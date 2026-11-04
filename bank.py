
class Bank:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""
        self.Aadhar_number = 0
        self.balance = 0

    # 1. Create Bank Account
    def create_account(self):
        print("\n----- Create Bank Account -----")

        self.name = input("Enter Account Holder Name: ")

        while True:
            self.phone = input("Enter Phone Number: ")
            if self.phone.isdigit() and len(self.phone)==10:
                break

            else:
                print("enter caret Phone Number")
        
        while True:
            self.Aadhar_number = input("Enter Aadhar Number: ")
            if self.Aadhar_number.isdigit() and len(self.Aadhar_number)==12:
                break
            else:
                print("enter caret Aadhar Number")


        self.address = input("Enter Address: ")
        
        print("\nAccount Created Successfully!")

    # 2. Display Account Holder Details
    def display_details(self):
        print("\n----- Account Holder Details -----")
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Address:", self.address)
        print("Aadhar Number:", self.Aadhar_number)

    # 3. Deposit Money
    def deposit(self):
        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:
            self.balance += amount
            print("Money Deposited Successfully!")
        else:
            print("Invalid Amount!")

    # 4. Withdraw Money
    def withdraw(self):
        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Money Withdrawn Successfully!")
        else:
            print("Insufficient Bank Balance!")

    # 5. Check Bank Balance
    def check_balance(self):
        print("\nAvailable Bank Balance:", self.balance)


# Main Program

b1 = Bank()

while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Bank Account")
    print("2. Display Account Holder Details")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Bank Balance")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        b1.create_account()

    elif choice == 2:
        b1.display_details()

    elif choice == 3:
        b1.deposit()

    elif choice == 4:
        b1.withdraw()

    elif choice == 5:
        b1.check_balance()

    elif choice == 6:
        print("Thank You For Using Our Bank!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
