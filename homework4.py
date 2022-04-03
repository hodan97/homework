# Task 2(Exception Handling)
# Question 1
# Simple ATM program
# Using exception handling code blocks such as try/ except / else / finally,
# write a program that simulates an ATM machine to withdraw money.
# (NB: the more code blocks the better, but try to use at least two key words e.g. try/except)
# Tasks:
# 1.       Prompt user for a pin code - done
# 2.       If the pin code is correct then proceed to the next step, - done
# otherwise ask a user to type in a pin again. You can give a user a maximum of 3 attempts and then exit a program.
# 3.       Set account balance to 100. - done
# 4.       Now we need to simulate cash withdrawal - done
# 5.       Accept the withdrawal amount - done
# 6.       Subtract the amount from the account balance and
# display the remaining balance (NOTE! The balance cannot be negative!) - done
# 7.       However, when a user asks to ‘withdraw’ more money than they have on their account,
# then you need to raise an error an exit the program. - done


def pin_checker():
    pin_try = 0
    while pin_try < 3:
        pin_code = input("Please enter 4 digit pin code for ATM: ")
        if pin_code == '0000':
            balance = 100
            print("pin accepted")
            print("Your current balance is: {}".format(balance))
            break
        else:
            print("pin incorrect, try again!")
            pin_try += 1
    try:
        if pin_try == 3:
            raise Exception
    except:
        print("Card blocked pin tried 3 times!")
        exit()


pin_checker()


def withdraw_check():
    withdraw = int(input("Please enter amount you would like to withdraw: "))
    balance = 100
    try:
        if withdraw > balance:
            raise Exception
    except:
        print(
            "Balance cannot be negative so withdrawal not accepted,"
            " withdraw needs to be less than balance or equal to balance")
    else:
        balance = balance - withdraw
        print("You withdrew :{}".format(withdraw))

        print("Your now current balance is: {}".format(balance))
    finally:
        if balance == 100:
            print("Your balance stays as: {}".format(balance))


withdraw_check()
