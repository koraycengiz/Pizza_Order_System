import csv
import datetime

from Pizza import Pizza, TurkishPizza, ClassicPizza, MargheritaPizza, DominosPizza, Decorator

# A counter to hold total cost.
total_cost = 0
# A string to hold the ingredients of the pizza.(beef,onion,mushroom...)
toppingCounter = ""
order = ""
pizzaCounter = 1

# This variable checks if the order is finished or not.
isComplete = True

while True:

    # read the Menu file
    f = open("Menu.txt", "r")
    print(f.read())

    selectedPizza = Pizza()

    while True:

        # Choose a pizza and according to chosen pizza , a new appropriate pizza object created.
        pizza = input("Pizza Base: ").lower().strip()

        if pizza == "1" or pizza == "classic":
            selectedPizza = ClassicPizza()
            total_cost = total_cost + selectedPizza.get_cost()
            break

        elif pizza == "2" or pizza == "margherita":
            selectedPizza = MargheritaPizza()
            total_cost = total_cost + selectedPizza.get_cost()
            break

        elif pizza == "3" or pizza == "turkish":
            selectedPizza = TurkishPizza()
            total_cost = total_cost + selectedPizza.get_cost()
            break

        elif pizza == "4" or pizza == "dominos":
            selectedPizza = DominosPizza()
            total_cost = total_cost + selectedPizza.get_cost()
            break

        else:
            print("This is not a valid option. Please try again.")

    # A loop for ingredients.
    flag = True
    while flag:
        try:
            toppings = int(input("Preferred toppings? ").strip())

            # If the user presses 0 , there will be no more topping.
            if toppings == 0:
                break

            elif toppings > 16 or toppings < 11:
                print("Invalid number. Please try again.")
                continue
        except NameError:
            print("You have to enter a number.")
            continue
        except ValueError:
            print("You have to enter a number.")
            continue


        else:
            decorator = Decorator(toppings)
            # According to appropriate topping , total_cost will hold it's cost plus the pizza cost.
            total_cost = total_cost + decorator.get_cost()
            # A small description for pizzas and their ingredients.
            toppingCounter = toppingCounter + " with " + decorator.get_description() + ", "

        answer = input("Do you like to add more? yes/no").lower().strip()

        if answer == "no":
            flag = False
        elif answer == "yes":
            continue
        else:
            print("Invalid option")
            break

    print()

    # Tells what is user's order.
    order = order + selectedPizza.get_description() + toppingCounter
    print(order)
    print()
    print(f"Total cost is : {total_cost}")

    isContinuous = input("Do you like to finish your order ? yes/no").lower().strip()
    if isContinuous == "yes":
        isContinuous = False
        break
    elif isContinuous == "no":
        selection = input("Do you like to order again? yes/no").lower().strip()
        if selection == "no":
            print("We are sorry to tell you that your order is canceled")
            isContinuous = False
            isComplete = False
            break
        else:
            try:
                selection2 = int(input("Press 1 to change your ordered pizza.\nPress 2 to order one more pizza."))
                if selection2 == 1:
                    # Resets the total cost and the topping counter to refresh the order.
                    total_cost = 0
                    order = ""
                    toppingCounter = ""

                else:
                    # If the user wants to add another pizza ,this block resets the ingredient holder(toppingCounter).
                    toppingCounter = ""
                    pizzaCounter = pizzaCounter + 1


            except ValueError:
                print("Please enter a valid option.")
    else:
        print("Invalid option. Your order has been canceled. Please order again.")
        total_cost = 0
        print()

# If order has completed, payment will begin.
if isComplete:
    user_name = input("Please type your user name")
    user_id = input("Please type your user id")
    credit_card = input("Please type your credit card number")
    card_password = input("Please type your credit card password")
    order_time = datetime.datetime.now()
    data = [order, user_name, user_id, credit_card, card_password]
    information_list = []
    # open the file in the write mode

    f = open('Orders_Database.csv', 'a')
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file

    # skip first row

    # make Into fields
    information_list.append({
        'Order Information': data[0],
        'User name': data[1],
        'user id': data[2],
        'Credit Card Number': data[3],
        'Credit Card Password': data[4],
    })
    information = [information_list, order_time]
    writer.writerow(information)
    # close the file
    f.close()

    print("**************************")
    print("WE RECEIVED YOUR ORDER. THANK YOU... ")
    print("WAITING TIME IS APPROXIMATELY 20-30 MINUTES... HAVE A NICE DAY")
