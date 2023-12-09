#Validating string input for password - case sensitive
PASSWORD = "Codetown"

def is_valid_string_input(value, valid_values):
    return value in valid_values

def get_password():
    while True:
        attempt = input("Enter your password to open the self-check-in register: ")
        if attempt == PASSWORD:
            return True
        else:
            print("Incorrect password. Please try again.")
            
#validating string input for day values - case insensitive
def get_valid_day(attempt):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if is_valid_string_input(attempt.capitalize(), days):
            #capitalise any user inputs entered in lowercase
            print(f'Thank you! The self check-in counter is now open. (day: {attempt.capitalize()})') 
            return False
    else:
        print("Invalid day entered. Try again, for example 'Sunday'.")
        return True 
    
today = ""
if get_password():
    print("Hello Operator!")
    session_timed_out = True
    while session_timed_out == True:
        today = input("Please enter the day of the week: ")
        session_timed_out = get_valid_day(today)           

def print_menu(menu_options):
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            user_input = int(input("Please, enter your choice: "))
            print()
            if 1 <= user_input <= len(menu_options):
                return user_input
            else:
                print("Invalid selection! Please try again.")
                print()
        except ValueError:
            print("Invalid input. Please enter a number.")
            print()

# Function to validate and convert input weight to a float
def validate_weight(input_weight):
    try:
        weight = float(input_weight)
        if weight > 0:
            return weight
        else:
            print("Invalid input! Please enter a valid positive number.")
            print()
            return False
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        print()
        return False

#Calculate subtotal before applying discounts
def compute_subtotal(kg_purchased, cost_per_kg, applicable_discounts, green_card_surcharge): 
    subtotal = kg_purchased * cost_per_kg
    print( str(kg_purchased) + ' Kilos X $' + str(cost_per_kg) + ': $' + str(round(subtotal, 2)))

    #Calculate total discount
    total_discount = 0.0
    for discount in applicable_discounts:
        current_discount = subtotal * (discount)
        subtotal -= current_discount 
        total_discount += current_discount
        
    #Apply discounts and surcharge to subtotal
    print('Applicable discount: ' + '-$' + str(round(total_discount, 2)))

    #Calculate total for green card surcharge
    surcharge_total = 0
    if green_card_surcharge == True:
        surcharge_total = subtotal * 0.05
        print('Applicable surcharge: ' + '$' + str(round(surcharge_total, 2)))
        subtotal += surcharge_total
    print('Final price: ' + '$' + str(round(subtotal, 2)))
    print()
    
    #Return results as a tuple
    return round(kg_purchased * cost_per_kg, 2), round(total_discount, 2), round(surcharge_total)

if __name__ == "__main__": 
    main_menu_loop = True

    while main_menu_loop == True:
        # Entering store menu
        print()
        print("Welcome to Codetown's Grocery Store!")

        finish_shop = False

        store_menu_options = ["Start registering your grocery", "Close the self-check-in register"]
        user_choice = print_menu(store_menu_options)
    

        #Enter discount cards once only
        pensioner_card_applied = False 
        weekend_card_applied = False
        green_card_applied = False

        #Cart_list: Setting to cost to 0 so cart list is by default empty
        cart_list = {'Apples': 0, 'Bananas': 0, 'Meat': 0, 'Fish': 0}

        if user_choice == 1:
            # Entering the Registration Menu
            registration_menu_options = ["Add a discount card", "Register a new item", "Compute total and pay"]
            while finish_shop == False:
                registration_choice = print_menu(registration_menu_options)
            
                if registration_choice == 1:
                    # Adding discount cards
                        discount_cards = ['Pensioner', 'Weekend', 'Green']
                        card_choice = print_menu(discount_cards)
                        if card_choice == 1:
                            if pensioner_card_applied == False:
                                pensioner_card_applied = True
                                print(f"The {discount_cards[card_choice - 1]} Card has successfully been added!")
                                print()
                            else:
                                print(f'Invalid selection! You have already added the {discount_cards[card_choice - 1]} Card.')
                                print()
                        elif card_choice == 2:
                            if weekend_card_applied == False:
                                weekend_card_applied = True
                                print(f"The {discount_cards[card_choice - 1]} Card has successfully been added!")
                                print()
                            else:
                                print(f'Invalid, already applied please try again.')
                                print()
                        elif card_choice == 3:
                            if green_card_applied == False:
                                green_card_applied = True
                                print(f"The {discount_cards[card_choice - 1]} Card has successfully been added!")
                                print()
                            else:
                                print(f'Invalid, already applied please try again.')
                                print()
                    
                elif registration_choice == 2:
                    # Registering items
                    items = ['Apples', 'Bananas', 'Meat', 'Fish']
                    item_choice = print_menu(items)
                    item_name = items[item_choice - 1]

                    item_weight = float(input(f"How many kilos of {item_name} do you want to register: "))
                    validated_weight = validate_weight(item_weight)
                    if validated_weight:
                    #Format to two decimal places
                        print(f"Successfully added {round(item_weight, 2)} kilos of {item_name} to your grocery!")
                        print()
                        if item_name == 'Apples':
                            cart_list["Apples"] += item_weight
                        if item_name == 'Bananas':
                            cart_list["Bananas"] += item_weight
                        if item_name == 'Meat':
                            cart_list['Meat'] += item_weight
                        if item_name == 'Fish':
                            cart_list['Fish'] += item_weight

                elif registration_choice == 3:
                    # Compute total and pay logic
                    finish_shop = True
                    cost_per_kg = {'Apples': 5, 'Bananas': 3, 'Meat': 20, 'Fish': 17}
                    applicable_discounts = []
                
                    items = ['Apples', 'Bananas', 'Meat', 'Fish']

                    subtotal = 0 
                    for x in items:
                        green_card_surcharge = False
                        if pensioner_card_applied:
                            applicable_discounts.append(0.1)
                        if weekend_card_applied and (today == 'Saturday' or today == 'Sunday'):
                            applicable_discounts.append(0.075)
                        if green_card_applied:
                            if x == 'Apples' or x == 'Bananas':
                                applicable_discounts.append(0.15)
                            else:
                                green_card_surcharge = True
                        if cart_list[x] != 0:
                            print(x + ':')
                            temp_subtotal = compute_subtotal(cart_list[x], cost_per_kg[x], applicable_discounts, green_card_surcharge)
                            amount = temp_subtotal[0] - temp_subtotal[1] + temp_subtotal[2]
                            subtotal += amount
                        
                    print('Total due: $' + str(subtotal))

                    checkout = input("Please, press Enter to proceed with the payment at the service desk: ")
                    
        if user_choice == 2:
            attempt = input("Enter your password to close the self-check-in register: ")
            if attempt == PASSWORD:
                print('Self-check-in counter successfully closed! Bye!')
                break
            else:
                print("Incorrect password. Please try again.")