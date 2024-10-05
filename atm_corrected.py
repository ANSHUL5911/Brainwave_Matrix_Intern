
from CardHolder_corrected import cardHolder

def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardholder):
    try:
        deposit = float(input("How much ₹ would you like to deposit: "))
        cardholder.set_balance(cardholder.get_balance() + deposit)
        print("Thank you for your ₹. Your new balance is: ", str(cardholder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardholder):
    try:
        withdraw = float(input("How much ₹ would you like to withdraw: "))
        ### Check if user has enough money
        if cardholder.get_balance() < withdraw:
            print("Insufficient balance :(")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdraw)
            print("You're good to go! Thank you :)")
    except:
        print("Invalid input")

def check_balance(cardholder):
    print("Your current balance is: ", cardholder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", 0)

    ### Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("6754832918456378", 1234, "Anshul", "Singh", 3515.45))
    list_of_cardHolders.append(cardHolder("6754832911244232", 2346, "Aditya", "Jadon", 515.65))
    list_of_cardHolders.append(cardHolder("1231278918456378", 8888, "Atreya", "Tiwari", 235.15))
    list_of_cardHolders.append(cardHolder("6754877777856378", 7434, "Aayush", "kumar", 999.80))
    list_of_cardHolders.append(cardHolder("6713621316186241", 1212, "Ranjeet", "Singh", 234.44))

    ### Prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.get_cardNum() == debitCardNum]

            if len(debitMatch) > 0:
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")

    ### Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your PIN: ").strip())
            if current_user.get_pin() == userPin:
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")

    ### Print options
    print("Welcome ", current_user.get_firstname(), " :)")

    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if option == 1:
            deposit(current_user)
        elif option == 2:
            withdraw(current_user)
        elif option == 3:
            check_balance(current_user)
        elif option == 4:
            break
        else:
            option = 0

    print("Thank you, Have a nice day :)")
