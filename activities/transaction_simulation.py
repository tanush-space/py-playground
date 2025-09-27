'''ATM Transaction Simulation
Inputs: account_balance, amount_to_withdraw, account_type (Saving/Current), day (weekday/weekend).
Rules:
•	Withdrawal allowed only if balance ≥ withdrawal + 1000 (minimum balance).
•	Weekend transactions charge extra ₹50 fee.
•	Saving account daily limit = 25,000; Current account = 50,000.
Output: Success/Failure with reason and updated balance.
'''
bal = float(input("Enter account balance: "))
amt = float(input("Enter amount to withdraw: "))
atype = input("Account type (Saving/Current): ").lower()
day = input("Day (weekday/weekend): ").lower()

fee = 0
limit = 25000 if atype == "saving" else 50000

if day == "weekend":
    fee = 50

if amt > limit:
    print("Failure: Limit exceeded")
elif bal < amt + 1000 + fee:
    print("Failure: Insufficient balance (min 1000 must remain)")
else:
    bal -= amt + fee
    print("Success: Withdrawn ₹", amt)
    if fee > 0:
        print("Weekend fee ₹", fee)
    print("Updated Balance = ₹", bal)
