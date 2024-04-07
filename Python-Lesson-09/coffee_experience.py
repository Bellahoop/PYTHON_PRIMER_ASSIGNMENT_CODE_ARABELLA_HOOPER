from coffee_and_code import SmartCoffeeMachine

def testing(): 
    brand = input("Enter the Smart Coffee Machine brand: ")
    model_number = input("Enter the Smart Coffee Machine model number: ")
    my_coffee_machine = SmartCoffeeMachine(model_number, brand)

    my_coffee_machine.report()

    while True:
        print("\nHow can I help you today?")
        print("1. List menu items")
        print("2. Update Menu")
        print("3. Make Coffee")
        print("4. Exit")
        
        choice = input("Enter your numeric choice (1, 2, 3, or 4): ")
        
        if choice == '1':
            my_coffee_machine.list_menu()
            menu_action = input("\nWould you like to add to the menu, make a coffee, or exit? (add/make/exit): ").lower()
            if menu_action == 'add':
                new_coffee = input("Please enter the new coffee to add to the menu: ")
                my_coffee_machine.update_menu(new_coffee)
            elif menu_action == 'make':
                coffee_type = input("Please enter the coffee type to make: ")
                my_coffee_machine.make_coffee(coffee_type)
            elif menu_action == 'exit':
                continue
            else:
                print("Invalid choice.")
        elif choice == '2':
            new_coffee = input("Please enter the new coffee to add to the menu: ")
            my_coffee_machine.update_menu(new_coffee)
            my_coffee_machine.list_menu()
            menu_action = input("\nWould you like to add anything else, make a coffee, or exit? (add/make/exit): ").lower()
            if menu_action == 'add':
                new_coffee = input("Please enter another new coffee to add to the menu: ")
                my_coffee_machine.update_menu(new_coffee)
            elif menu_action == 'make':
                coffee_type = input("Please enter the coffee type to make: ")
                my_coffee_machine.make_coffee(coffee_type)
            elif menu_action == 'exit':
                continue
            else:
                print("Invalid choice.")
        elif choice == '3':
            coffee_type = input("Please enter the coffee type to make: ")
            my_coffee_machine.make_coffee(coffee_type)
        elif choice == '4':
            print("Exiting, please run this code again if you wish to change your choice.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    testing()