import sys
import random
import time
import signal

delay = random.randrange(2, 6)

feedback_phrases_rc = [
    "Certainly!",
    "Of course!",
    "Absolutely!",
    "Right away!",
    "No problem!",
    "Sure thing!",
    "Gladly!",
    "My pleasure!",
    "You got it!",
    "I'm happy to help!"
]

feedback_phrases_processing = [
    "We're working on it...",
    "Hold on a moment, please...",
    "Your request is being processed...",
    "Just a little longer...",
    "We're working to complete your request...",
    "Processing can take a few moments...",
    "Just a few more seconds...",
    "Your request is in progress."
]

feedback_phrases_q = [
    "Alright! Thank you, have a great day!",
    "Goodbye!",
    "See you later!",
    "Take care!",
    "Have a nice day!",
    "Farewell!",
    "Hope to see you again soon!",
    "Have a wonderful day ahead!",
    "It was nice talking to you!",
    "Stay safe and healthy!"
]
feedback_phrases_invalid = [
    "Sorry, I didn't understand that.",
    "I'm not sure what you mean.",
    "Please try again.",
    "Invalid input.",
    "That's not a valid option.",
    "Try something else.",
    "We didn't quite catch that. Please rephrase your input.",
    "Hmmm, looks like we hit a snag there. Can you try that again?",
    "It seems like there was a problem with your input. Please try again.",
    "Oops! Looks like something went wrong. Please check your input and try again."
]
feedback_phrases_pick = [
    "Sorry, that's an invalid choice. Please choose a number from 1 to 4.",
    "We're sorry, but the options are limited to numbers 1 through 4. Please try again.",
    "Invalid input. Remember to choose a number between 1 and 4 only.",
    "It seems like you entered an incorrect value. Please select a number from 1 to 4.",
    "The selection must be a number from 1 to 4. Please try again.",
    "Oops! Looks like you entered an invalid value. Please choose a number between 1 and 4 only.",
    "That's not a valid input. Please select a number from 1 to 4.",
    "Invalid choice. The available options are only numbers 1 through 4.",
    "We're sorry, but the selection you entered is not valid. Please try again with a number from 1 to 4.",
    "It seems like you entered an incorrect value. Remember to select a number from 1 to 4 only."
]
feedback_phrases_ibalance = [
    "Looks like you don't have enough funds for that order.",
    "Sorry, your balance is too low to place this order.",
    "You need more funds to place this order.",
    "Insufficient balance.",
    "Unfortunately, you do not have enough balance for this order.",
    "Your balance is too low to place this order.",
    "We're sorry, you don't have sufficient funds for this transaction.",
    "You need more money in your account to complete this transaction.",
    "Your balance is too low for this transaction.",
    "Insufficient funds."
]

feedback_phrases_commend = [
    "Great!",
    "Good!",
    "Nice!",
    "Perfect!",
    "Excellent!",
    "Cool!",
    "Alright!"
]

feedback_phrases_choice = [
    "Excellent Choice!",
    "You must have a good taste!",
    "Great choice!",
    "Excellent decision!",
    "You picked a winner!",
    "Fantastic selection!",
    "Impressive choice!",
    "You have great taste!",
    "Spot on choice!",
    "You made the right call!",
    "Brilliant choice!",
    "Top-notch decision!"
]

print("Welcome to My Bakeshop! To Begin, Kindly")
def get_balance():
    while True:
        balance = input("Type in your balance: $")
        print(random.choice(feedback_phrases_processing))
        time.sleep(delay)
        if balance.isnumeric():
            balance = float(balance)
            if balance < 10:
                while True:
                    answer = input("Press R to Re-enter Balance or Q to Quit: ")
                    answer = answer.capitalize()
                    if answer == "R":
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(random.choice(feedback_phrases_rc))
                        return get_balance()
                    elif answer == "Q":
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(random.choice(feedback_phrases_q))
                        sys.exit()
                    else:
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(random.choice(feedback_phrases_invalid))
                        print("Sorry, but you have insufficient balance!")
            else:
                menu = {'1': ['Bread', 10], '2': ['Pancake', 20], '3': ['Cupcake', 40], '4': ['Cake', 60]}
                print(f"{random.choice(feedback_phrases_commend)} Here's our menu:")
                for order, (item, price) in menu.items():
                    print(f"{order}. {item} = ${price}")
                balance_range_messages = {
                    (10, 19): "With your balance, you can only buy Bread.",
                    (20, 39): "With your balance, you can only buy Bread and Pancake.",
                    (40, 59): "With your balance, you can only buy Bread, Pancake, and Cupcake.",
                    (60, float('inf')): "With your balance, you can buy Bread, Pancake, Cupcake, and Cake."
                }
                for balance_range, message in balance_range_messages.items():
                    if balance_range[0] <= balance < balance_range[1]:
                        print(message)
                        break
            return balance
        else:
            print(random.choice(feedback_phrases_processing))
            time.sleep(delay)
            print(random.choice(feedback_phrases_invalid))


menu = {'1': 10.0, '2': 20.0, '3': 40.0, '4': 60.0}

def order():
    balance = get_balance()
    while True:
        order = input("Type the number of your order: ")
        if order in menu:
            order_number = order
            if balance >= menu[order]:
                print(random.choice(feedback_phrases_processing))
                time.sleep(delay)
                print(random.choice(feedback_phrases_choice))
                print(f"Order #{order_number} costs ${menu[order]}.")
                while True:
                    answer = input("Press P to Proceed, C to Cancel and Change Order, or Q to Quit: ")
                    answer = answer.capitalize()
                    if answer == "C":
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(random.choice(feedback_phrases_rc))
                    elif answer == "P":
                        balance -= menu[order_number]
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(f"Transaction complete! Remaining balance is ${balance}" '\n' "Enjoy!")
                        return
                    elif answer == "Q":
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(random.choice(feedback_phrases_q))
                        sys.exit()
                    else:
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(random.choice(feedback_phrases_invalid))
            else:
                balance_range_messages = {
                    (0, 19): f"{random.choice(feedback_phrases_ibalance)} You can only choose order #1.",
                    (20, 39): f"{random.choice(feedback_phrases_ibalance)} You can only choose order #1 and #2.",
                    (40, 59): f"{random.choice(feedback_phrases_ibalance)} You can only choose order #1, #2 and #3.",
                }
                for balance_range, message in balance_range_messages.items():
                    if balance_range[0] <= balance <= balance_range[1]:
                        print(random.choice(feedback_phrases_processing))
                        time.sleep(delay)
                        print(message)
                        break
        else:
            print(random.choice(feedback_phrases_processing))
            time.sleep(delay)
            print(random.choice(feedback_phrases_pick))
order()

#To-do: Work on developing more alternative phrases, and work for website building
