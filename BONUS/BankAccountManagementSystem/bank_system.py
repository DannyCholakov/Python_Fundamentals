# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    # 2. Add the new account holder to the list of account holders.
    account_holders.append(input("Enter your account name: "))
    # 3. Initialize the balance to 0 for the new account.
    balances.append(0)
    # 4. Initialize an empty transaction history for the new account.
    transaction_histories.append(0)
    # 5. Initialize the outstanding loan amount to 0.
    loans.append(0)
    # 6. Notify the user of the successful account creation.
    print('Your account is created successfully.')
    print('Returning to Display menu.')
    input('Press Enter to continue...')
    main()

def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    account_holder_check = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if account_holder_check in account_holders:
    # 3. If the account exists, prompt the user for the amount to deposit.
    # 4. Update the account's balance with the deposited amount.
        balances[account_holders.index(account_holder_check)] += float(input("How much would you like to deposit?: "))
    # 5. Log the transaction in the account's transaction history.
        transaction_histories[account_holders.index(account_holder_check)] += 1
    # 6. Display the updated balance to the user.
        print('New balance: '+ str(balances[account_holders.index(account_holder_check)]))
    # 7. If the account does not exist, inform the user.
    else:
        print('There is no account with that name.')

    input('Press Enter to continue...')
    main()

def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    account_holder_check = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if account_holder_check in account_holders:
        # 3. If the account exists, prompt the user for the amount to withdraw.
        withdraw_amount = float(input("How much would you like to withdraw?: "))
        # 4. Check if there are sufficient funds for the withdrawal.
        if balances[account_holders.index(account_holder_check)] >= withdraw_amount:
            # 5. If funds are sufficient, update the balance and log the transaction.
            balances[account_holders.index(account_holder_check)] -= withdraw_amount
            transaction_histories[account_holders.index(account_holder_check)] += 1
            # 6. Display the updated balance to the user.
            print('New balance: ' + str(balances[account_holders.index(account_holder_check)]))
        else:
            # 7. If insufficient funds, inform the user.
            print('Insufficient funds.')
    else:
        # 8. If the account does not exist, inform the user.
        print('There is no account with that name.')

    input('Press Enter to continue...')
    main()

def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    account_holder_check = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if account_holder_check in account_holders:
    # 3. If the account exists, display the current balance.
        print('current balance: ' + str(balances[account_holders.index(account_holder_check)]))
    # 4. If the account does not exist, inform the user.
    else:
        print('There is no account with that name.')

    input('Press Enter to continue...')
    main()


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if len(account_holders) > 0:
    # 2. If there are accounts, loop through each account holder.
    # 3. Display the account holder's name, balance, and outstanding loan amount.
        for account_holder in account_holders:
            print('----------------')
            print('Account Name: ' + account_holder)
            print('Balance: ' + str(balances[account_holders.index(account_holder)]))
            print('Loan Amount: ' + str(loans[account_holders.index(account_holder)]))
            print('----------------')
    # 4. If there are no accounts, inform the user.
    else:
        print('There are no accounts in the system.')

    input('Press Enter to continue...')
    main()


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender_name = input("Enter sender's name: ")
    receiver_name = input("Enter receiver's name: ")
    # 2. Check if both accounts exist in the system.
    if sender_name in account_holders and receiver_name in account_holders:
    # 3. If both accounts exist, prompt the user for the amount to transfer.
        transfer_amount = float(input("How much would you like to transfer?: "))
    # 4. Check if the sender has sufficient funds for the transfer.
        if balances[account_holders.index(sender_name)] >= transfer_amount:
    # 5. If funds are sufficient, update both balances and log the transactions.
            balances[account_holders.index(sender_name)] -= transfer_amount
            balances[account_holders.index(receiver_name)] += transfer_amount
            transaction_histories[account_holders.index(sender_name)] += 1
            transaction_histories[account_holders.index(receiver_name)] += 1
    # 6. Inform the user of the successful transfer.
            print(f'Transfer for {transfer_amount} complete.')
    # 7. If insufficient funds or if either account does not exist, inform the user.
        else:
            print('Insufficient funds.')
    else:
        print('There is/are no accounts with that name.')

    input('Press Enter to continue...')
    main()

def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    account_holder_check = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if account_holder_check in account_holders:
    # 3. If the account exists, display the transaction history.
        if transaction_histories[account_holders.index(account_holder_check)] > 0:
            print('Transactions made: '+ str(transaction_histories[account_holders.index(account_holder_check)]))
    # 4. If there are no transactions, inform the user.
        else:
            print('This account has not made any transactions.')
    # 5. If the account does not exist, inform the user.
    else:
        print('There is no account with that name.')

    input('Press Enter to continue...')
    main()

def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")
    input('Press Enter to continue...')
    main()


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")
    input('Press Enter to continue...')
    main()


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")


main()