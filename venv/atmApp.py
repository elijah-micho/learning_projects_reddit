def atmApp():
    account_num = "123456"
    pin_num = "7890"
    acc_match = False
    pin_match = False

    while acc_match == False:
        user_acc = str(input("Enter your account number: "))
        if user_acc == account_num:
            print("Account number is correct!")
            acc_match = True


            if acc_match == True:
                while pin_match == False:
                    user_pin = str(input("Enter your pin: "))
                    if user_pin == pin_num:
                        print("Pin number is correct!")
                        atmMenu()
                        exit()
                    else:
                        print("Pin is incorrect.")
        else:
            print("Account number is incorrect.")

class atmMenu():
    def __init__(self):
        self.acc_balance = 0
        menu_choice = str(input("Select an option:\n [1]Deposit \n [2]Withdrawl\n [3]Exit? \n"))

        if menu_choice == "1":
            self.deposit()
        elif menu_choice == "2":
            self.withdrawl()
        else:
            exit()

    def deposit(self):

        while True:
            user_deposit = int(input("How much would you like to deposit? "))
            self.acc_balance += user_deposit
            print("$%s has been deposited into your account. " %(user_deposit,))

            user_choice = str(input("Do you want to make another deposit? Type Yes or No: "))

            if user_choice == "No":
                print("Ending transaction")
                break


    def withdrawl(self):
        while True:
            user_withdrawl = int(input("How much would you like to withdraw? "))
            self.acc_balance -= user_withdrawl
            print("$%s has been withdrawn from your account." %(user_withdrawl,))

            user_choice = str(input("Do you want to make another deposit? Type Yes or No: "))

            if user_choice == "No":
                print("Ending transaction")
                break

    def __exit__(self, exc_type, exc_val, exc_tb):
        exit()
atmApp()

