'''
  ----------------------------------------------------------------------------------------------------
**  Name: Carl F. Blancaflor                                                                         **
**  Section: BscPe 1-5                                                                               **
**  Subject: Programming logic and design                                                            **
**  Professor: Mr. Cansino                                                                           **
**  Title: Snack Bar                                                                                 **
**---------------------------------------------------------------------------------------------------**

This program simulates a Point-of-Sales terminal for a fine dining called Snack bar.
it allows the user to interact with a programmed waiter and choose their desired order from the menu.
after the user inputs their order, the programmed waiter will ask for the amount of money the user will pay.
finally, the program will display the receipt of the user's order with the added VAT on the total purchase included.

'''


#defining the prices of the items on the menu
hotdog = 45.50
hamburger = 35.75
frenchfries = 25.85
milkshake = 15.75
decision = ""

#defining the order dictionary
order = {
    "money": 0,
    "hotdog": 0, 
    "hamburger": 0, 
    "french fries": 0, 
    "milkshake": 0
    }

#making the menu interface
menu = (
    "\t<<<<<<< FINE DINING SNACK BAR >>>>>>>>>>\n\n"
    "\t            Menu for today \n\n"
    "\t----------------------------------------- \n"
    f"\t*\t Hotdog\t\t: Php{hotdog} \t*\n"
    f"\t*\t Hamburger\t: Php{hamburger} \t*\n"
    f"\t*\t French Fries\t: Php{frenchfries} \t*\n"
    f"\t*\t Milkshake\t: Php{milkshake} \t*\n"
    "\t-----------------------------------------\n")

#greetings for the user
print("\nWelcome to Snack Bar!! I am your waiter Carl, here is our menu:\n")
print(menu)


#adding a function for the user to input their order
def orderlist():
    while True:
        choice = input("\nWhat would you like to order? \n\nPlease enter the name from the menu: ").lower()
        if choice in order: #checking if the input is in the menu
            qty = int(input(f"\nHow many orders of {choice} would you like to order? "))
            order[choice] += qty
            decision = input('\nWould you like to order anything else? ("yes" or "no"): ').lower()
            
            if decision == "no": #after the user inputs all their desired order the program will display the total amount of the order and ask for the amount of money the user will pay
                grossprice = (hotdog * order['hotdog']) + (hamburger * order['hamburger']) + (frenchfries * order['french fries']) + (milkshake * order['milkshake'])
                vat = grossprice * 0.20 #formula for VAT which is 20% of the gross price
                totalamount = grossprice + vat 
                print(f'\nYour total price for your order is: Php{totalamount}\n')
                money = int(input("Please enter the amount of money you will pay: "))
                
                while True: #checking if the amount of money is enough
                    if money < totalamount:
                        print("Sorry, the amount you entered is not enough. Please enter the correct amount.")
                        money = int(input("Please enter the amount of money you will pay: "))
                    else:
                        break
                order["money"] = money
                break
            
        else:
            print("Sorry, we don't have that on the menu. Please choose from the list.")
    print("\nThank you for ordering! Here is your receipt:\n ")
    receipt()
    
    
#adding the receipt function and designing its interface
def receipt():
    totalqty = (f"\tEnter order of HotDog\t\t: {order['hotdog']}\n"
             f"\tEnter order of Hamburger\t: {order['hamburger']}\n"
             f"\tEnter order of French Fries\t: {order['french fries']}\n"
             f"\tEnter order of Milkshake\t: {order['milkshake']}\n")  
    grossprice = (hotdog * order['hotdog']) + (hamburger * order['hamburger']) + (frenchfries * order['french fries']) + (milkshake * order['milkshake'])
    vat = grossprice * 0.20
    totalamount = grossprice + vat
    total = (
        "\t<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>\n\n"
        f"\tHotdog\t\t: Php{hotdog} x {order['hotdog']} = Php{hotdog * order['hotdog']}\n"
        f"\tHamburger\t: Php{hamburger} x {order['hamburger']} = Php{hamburger * order['hamburger']}\n"
        f"\tFrench Fries\t: Php{frenchfries} x {order['french fries']} = Php{frenchfries * order['french fries']}\n"
        f"\tMilkshake\t: Php{milkshake} x {order['milkshake']} = Php{milkshake * order['milkshake']}\n\n"
        f"\tGross price\t= Php{grossprice}\n"
        f"\tw/VAT\t\t= Php{vat}\n"
        f"\tTotal Price\t= Php{totalamount}\n"
        f"\tAmount Tendered\t= Php{order['money']}\n"
        f"\tYour Change is\t= Php{order['money']- totalamount}\n\n"
        f"\tnumber of items sold: {order['hotdog'] + order['hamburger'] + order['french fries'] + order['milkshake']}\n\n"
        "\t**********THANK YOU FOR ORDERING**********\n\n" 
    )
    print(menu)
    print(totalqty)
    print(total)
    
    
#calling the orderlist function
orderlist()
