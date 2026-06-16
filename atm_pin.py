import time
import datetime
start_time = time.time()

hardcode = 1098
showbalance = 33562.23
currency = "rupees"
user_pin = int(input("Enter your pin:"))
if user_pin == hardcode:
    print("Pin is correct. Access granted.")
    print(f"Show balance: {showbalance} {currency}")
    print("withdraw money")

    withdrawal_money = float(input("Enter the amount you want to withdraw: "))
    if withdrawal_money <= showbalance:
        print("Please collect your cash.")
        print("\n" + "_"*10)
        print("please press your thumb at the pannel and collect you receipt")
        print("\n" + "_"*10)
        print("    receipt")
        print("   UNION BANK OF INDIA")
        print("date and time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("card number: **** **** **** 1234")
        print(f"withdrawal amount: {withdrawal_money}/-")
        print("from account:613002125486")
        print("surcharge: 12.05")
        print(f"available balance: {showbalance - withdrawal_money}/-")
        print("\n" + "_"*10)
    else:
        print("Insufficient balance!")
else:
    print("please enter correct pin:")
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")